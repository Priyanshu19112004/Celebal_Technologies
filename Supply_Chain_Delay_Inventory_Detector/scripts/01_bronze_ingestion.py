"""
==========================================================
Project : Supply Chain Delay & Inventory Mismatch Detector

Layer   : Bronze Layer

Author  : Priyanshu Tiwari

Purpose :
---------
This script reads all raw CSV files,
adds audit columns,
and stores them into the Bronze Layer
without modifying original data.

==========================================================
"""


# ==========================================================
# Import Required Libraries
# ==========================================================

import pandas as pd          # Data Processing
import json                  # Read Configuration File
import os                    # File Handling
from datetime import datetime # Current Timestamp


# ==========================================================
# Load Configuration File
# ==========================================================

# Open JSON configuration file
with open("config/pipeline_config.json", "r") as file:

    # Convert JSON into Python Dictionary
    config = json.load(file)


# ==========================================================
# Read Folder Locations from Config
# ==========================================================

# Dictionary containing all source file paths
sources = config["sources"]

# Bronze Folder Path
bronze_path = config["bronze_layer"]

# Pipeline Version
pipeline_version = config["version"]


# ==========================================================
# Create Bronze Folder if it doesn't exist
# ==========================================================

os.makedirs(bronze_path, exist_ok=True)


# ==========================================================
# Process Every Source File
# ==========================================================

for dataset_name, file_path in sources.items():

    print("=" * 60)

    print(f"Reading Dataset : {dataset_name}")

    # Read CSV
    df = pd.read_csv(file_path)

    print(f"Rows Loaded : {len(df)}")


    # ======================================================
    # Add Audit Columns
    # ======================================================

    # Timestamp when file was ingested
    df["_ingested_at"] = datetime.now()

    # Original Source File
    df["_source_file"] = os.path.basename(file_path)

    # Pipeline Version
    df["_pipeline_version"] = pipeline_version


    # ======================================================
    # Save into Bronze Layer
    # ======================================================

    output_file = os.path.join(

        bronze_path,

        f"bronze_{dataset_name}.csv"

    )

    df.to_csv(output_file, index=False)

    print(f"Saved : {output_file}")

    print("=" * 60)


print("\n")

print("Bronze Layer Completed Successfully")