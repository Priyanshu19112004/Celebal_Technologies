"""
===============================================================
Project : Supply Chain Delay & Inventory Mismatch Detector

Layer   : Silver Layer

Author  : Priyanshu Tiwari

Purpose :
----------
This script reads data from the Bronze Layer,
performs data quality validation,
moves invalid records to Quarantine,
cleans valid records,
and stores the cleaned data into the Silver Layer.

===============================================================
"""

# =============================================================
# Import Required Libraries
# =============================================================

import pandas as pd          # Data Processing
import json                  # Read JSON Config File
import os                    # File Handling
from datetime import datetime

# =============================================================
# Load Configuration File
# =============================================================

def load_config():
    """
    Load pipeline configuration from JSON file.

    Returns:
        dict : Configuration Dictionary
    """

    with open("config/pipeline_config.json", "r") as file:

        config = json.load(file)

    return config

# =============================================================
# Load Bronze Dataset
# =============================================================

def load_bronze_data(file_path):
    """
    Reads Bronze CSV file.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    DataFrame
    """

    print(f"\nReading : {file_path}")

    df = pd.read_csv(file_path)

    print(f"Rows Loaded : {len(df)}")

    return df

# =============================================================
# Create Folder Automatically
# =============================================================

def create_folder(folder_path):
    """
    Create folder if it doesn't exist.
    """

    os.makedirs(folder_path, exist_ok=True)

    # =============================================================
# Validate Dataset
# =============================================================

def validate_data(df, dataset_name):
    """
    Validate the dataset and separate valid & invalid records.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    dataset_name : str
        Name of dataset.

    Returns
    -------
    valid_df
    quarantine_df
    """

    # Copy dataframe
    data = df.copy()

    # New column to store failure reason
    data["_fail_reason"] = ""

    ############################################################
    # Rule 1 : Check Missing Values
    ############################################################

    if "supplier_id" in data.columns:

        data.loc[
            data["supplier_id"].isna(),
            "_fail_reason"
        ] += "Missing Supplier ID | "


    if "product_id" in data.columns:

        data.loc[
            data["product_id"].isna(),
            "_fail_reason"
        ] += "Missing Product ID | "


    ############################################################
    # Rule 2 : Negative Quantity
    ############################################################

    if "shipped_quantity" in data.columns:

        data.loc[
            data["shipped_quantity"] < 0,
            "_fail_reason"
        ] += "Negative Shipped Quantity | "


    if "received_quantity" in data.columns:

        data.loc[
            data["received_quantity"] < 0,
            "_fail_reason"
        ] += "Negative Received Quantity | "

        


    ############################################################
    # Rule : Zero Quantity
    ############################################################

    if "shipped_quantity" in data.columns:

        data.loc[
            data["shipped_quantity"] == 0,
            "_fail_reason"
        ] += "Zero Shipped Quantity | "

    if "received_quantity" in data.columns:

        data.loc[
            data["received_quantity"] == 0,
            "_fail_reason"
        ] += "Zero Received Quantity | "


    ############################################################
    # Rule : Active Supplier
    ############################################################

    if "is_active" in data.columns:

        data.loc[
            data["is_active"] == False,
            "_fail_reason"
        ] += "Inactive Supplier | "


    ############################################################
    # Rule : Supplier Rating
    ############################################################

    if "rating" in data.columns:

        data.loc[
            (data["rating"] < 1) |
            (data["rating"] > 5),
            "_fail_reason"
        ] += "Invalid Supplier Rating | "    


    ############################################################
    # Rule 3 : Invalid Dates
    ############################################################

    date_columns = [

        "dispatch_date",

        "expected_delivery_date",

        "actual_receipt_date",

        "contract_start_date",

        "contract_end_date"

    ]


    for column in date_columns:

        if column in data.columns:

            data[column] = pd.to_datetime(

                data[column],

                errors="coerce"

            )

            data.loc[

                data[column].isna(),

                "_fail_reason"

            ] += f"Invalid {column} | "


    ############################################################
    # Separate Valid & Invalid Records
    ############################################################

    valid_df = data[

        data["_fail_reason"] == ""

    ].copy()

    quarantine_df = data[

        data["_fail_reason"] != ""

    ].copy()

    return valid_df, quarantine_df


# =============================================================
# Remove Duplicate Records
# =============================================================

def remove_duplicates(df):
    """
    Remove duplicate records from dataset.

    Rules
    -----
    1. shipment_id -> Keep latest record
    2. receipt_id -> Keep latest record
    3. supplier_id -> Keep first record
    4. product_id -> Keep first record

    Returns
    -------
    DataFrame
    """

    data = df.copy()

    before = len(data)

    # Shipment Dataset
    if "shipment_id" in data.columns:

        data = data.drop_duplicates(
            subset="shipment_id",
            keep="last"
        )

    # Warehouse Dataset
    elif "receipt_id" in data.columns:

        data = data.drop_duplicates(
            subset="receipt_id",
            keep="last"
        )

    # Supplier Dataset
    elif "supplier_id" in data.columns:

        data = data.drop_duplicates(
            subset="supplier_id",
            keep="first"
        )

    # Product Dataset
    elif "product_id" in data.columns:

        data = data.drop_duplicates(
            subset="product_id",
            keep="first"
        )

    after = len(data)

    print("--------------------------------------")
    print("Duplicate Removal")
    print("--------------------------------------")
    print(f"Rows Before : {before}")
    print(f"Rows After  : {after}")
    print(f"Duplicates Removed : {before-after}")

    return data

# =============================================================
# Standardize Date Columns
# =============================================================

def standardize_dates(df):
    """
    Convert all date columns
    into YYYY-MM-DD format.
    """

    data = df.copy()

    date_columns = [

        "dispatch_date",

        "expected_delivery_date",

        "actual_receipt_date",

        "contract_start_date",

        "contract_end_date"

    ]

    for column in date_columns:

        if column in data.columns:

            data[column] = pd.to_datetime(

                data[column],

                errors="coerce"

            ).dt.strftime("%Y-%m-%d")

    print("Dates Standardized Successfully")

    return data

# =============================================================
# Save Clean Data and Quarantine Data
# =============================================================

def save_data(valid_df, quarantine_df, dataset_name, config):
    """
    Save valid records into Silver Layer
    and invalid records into Quarantine Layer.

    Parameters
    ----------
    valid_df : pandas.DataFrame
        Clean records

    quarantine_df : pandas.DataFrame
        Invalid records

    dataset_name : str
        Dataset name

    config : dict
        Configuration dictionary
    """

    # Read folder paths from config
    silver_path = config["silver_layer"]
    quarantine_path = config["quarantine_layer"]

    # Create folders if not available
    create_folder(silver_path)
    create_folder(quarantine_path)

    # Create output file names
    silver_file = os.path.join(
        silver_path,
        f"silver_{dataset_name}.csv"
    )

    quarantine_file = os.path.join(
        quarantine_path,
        f"quarantine_{dataset_name}.csv"
    )

    # Save Clean Data
    valid_df.to_csv(
        silver_file,
        index=False
    )

    # Save Invalid Data
    quarantine_df.to_csv(
        quarantine_file,
        index=False
    )

    print("\n------------------------------------------")
    print(f"Dataset : {dataset_name}")
    print(f"Total Records      : {len(valid_df)+len(quarantine_df)}")
    print(f"Valid Records      : {len(valid_df)}")
    print(f"Invalid Records    : {len(quarantine_df)}")
    print(f"Silver File        : {silver_file}")
    print(f"Quarantine File    : {quarantine_file}")
    print("------------------------------------------")

    # =============================================================
# Main Function
# =============================================================

def main():

    print("=" * 60)
    print("Starting Silver Layer Transformation")
    print("=" * 60)

    # Load configuration
    config = load_config()

    # Bronze folder path
    bronze_path = config["bronze_layer"]

    # Process every dataset
    for dataset_name in config["sources"].keys():

        file_path = os.path.join(
            bronze_path,
            f"bronze_{dataset_name}.csv"
        )

        # Read Bronze data
        df = load_bronze_data(file_path)

    # Validate data
    valid_df, quarantine_df = validate_data(
     df,
     dataset_name
)

    # Save outputs
    save_data(
    valid_df,
    quarantine_df,
    dataset_name,
    config
)

    print("\n")
    print("=" * 60)
    print("Silver Layer Completed Successfully")
    print("=" * 60)


# =============================================================
# Program Entry Point
# =============================================================

if __name__ == "__main__":
    main()