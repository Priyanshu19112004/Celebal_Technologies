"""
=============================================================
Project : Supply Chain Delay & Inventory Mismatch Detector

Layer   : Gold Layer

Author  : Priyanshu Tiwari

Purpose :
----------
This script reads cleaned Silver datasets,
detects business anomalies,
and generates analytics-ready Gold datasets.

Outputs
--------
1. Ghost Shipments
2. Phantom Receipts
3. Quantity Mismatch
4. Delivery Delay
5. Supplier Scorecard

=============================================================
"""

# ============================================================
# Import Libraries
# ============================================================

import pandas as pd
import json
import os


# ============================================================
# Load Config File
# ============================================================

def load_config():

    with open("config/pipeline_config.json","r") as file:

        config = json.load(file)

    return config


# ============================================================
# Read Silver Dataset
# ============================================================

def load_silver_data(config):

    silver_path = config["silver_layer"]

    shipments = pd.read_csv(

        os.path.join(

            silver_path,

            "silver_supplier_shipments.csv"

        )

    )

    receipts = pd.read_csv(

        os.path.join(

            silver_path,

            "silver_warehouse_receipts.csv"

        )

    )

    suppliers = pd.read_csv(

        os.path.join(

            silver_path,

            "silver_supplier_master.csv"

        )

    )

    products = pd.read_csv(

        os.path.join(

            silver_path,

            "silver_product_catalog.csv"

        )

    )

    return shipments,receipts,suppliers,products



# ============================================================
# Create Gold Folder
# ============================================================

def create_gold_folder(config):

    gold_path = config["gold_layer"]

    os.makedirs(

        gold_path,

        exist_ok=True

    )

    return gold_path


# ============================================================
# Ghost Shipment Detection
# ============================================================

def detect_ghost_shipments(shipments, receipts):

    """
    Find shipments that are dispatched
    but never received.
    """

    ghost = shipments[
        ~shipments["shipment_id"].isin(
            receipts["shipment_id"]
        )
    ].copy()

    print("--------------------------------------")
    print("Ghost Shipment Detection")
    print("--------------------------------------")
    print(f"Ghost Shipments Found : {len(ghost)}")

    return ghost


# ============================================================
# Phantom Receipt Detection
# ============================================================

def detect_phantom_receipts(shipments, receipts):

    """
    Find receipts without shipment.
    """

    phantom = receipts[
        ~receipts["shipment_id"].isin(
            shipments["shipment_id"]
        )
    ].copy()

    print("--------------------------------------")
    print("Phantom Receipt Detection")
    print("--------------------------------------")
    print(f"Phantom Receipts Found : {len(phantom)}")

    return phantom


# ============================================================
# Quantity Mismatch Detection
# ============================================================

def detect_quantity_mismatch(shipments, receipts):

    merged = shipments.merge(

        receipts,

        on="shipment_id",

        suffixes=("_ship", "_receive")

    )
    print("\nMerged Columns:")
    print(merged.columns.tolist())

    merged["difference_percent"] = (

        abs(

            merged["shipped_quantity"] -

            merged["received_quantity"]

        )

        /

        merged["shipped_quantity"]

    ) * 100

    mismatch = merged[

        merged["difference_percent"] > 5

    ]

    print("--------------------------------------")
    print("Quantity Mismatch Detection")
    print("--------------------------------------")
    print(f"Mismatches Found : {len(mismatch)}")

    return mismatch


# ============================================================
# Delivery Delay Detection
# ============================================================

def detect_delivery_delay(shipments, receipts):

    merged = shipments.merge(

        receipts,

        on="shipment_id"

    )

    merged["expected_delivery_date"] = pd.to_datetime(

        merged["expected_delivery_date"]

    )

    merged["actual_receipt_date"] = pd.to_datetime(

        merged["actual_receipt_date"]

    )

    merged["delay_days"] = (

        merged["actual_receipt_date"]

        -

        merged["expected_delivery_date"]

    ).dt.days

    delayed = merged[

        merged["delay_days"] > 3

    ]

    print("--------------------------------------")
    print("Delivery Delay Detection")
    print("--------------------------------------")
    print(f"Delayed Shipments : {len(delayed)}")

    return delayed


# ============================================================
# Supplier Scorecard
# ============================================================

def create_supplier_scorecard(shipments, delayed):

    """
    Create supplier performance scorecard.
    """

    # Total shipments per supplier
    total_shipments = shipments.groupby("supplier_id").size().reset_index(name="total_shipments")

    # Delayed shipments per supplier
    delayed_shipments = delayed.groupby("supplier_id").size().reset_index(name="delayed_shipments")

    # Merge both tables
    scorecard = total_shipments.merge(
        delayed_shipments,
        on="supplier_id",
        how="left"
    )

    # Replace NaN with 0
    scorecard["delayed_shipments"] = scorecard["delayed_shipments"].fillna(0)

    # Delay Percentage
    scorecard["delay_percentage"] = (
        scorecard["delayed_shipments"]
        /
        scorecard["total_shipments"]
    ) * 100

    # Supplier Score
    scorecard["supplier_score"] = (
        100 - scorecard["delay_percentage"]
    ).round(2)

    print("--------------------------------------")
    print("Supplier Scorecard")
    print("--------------------------------------")
    print(scorecard.head())

    return scorecard



# ============================================================
# Inventory Summary
# ============================================================

def create_inventory_summary(receipts):

    inventory = receipts.groupby("product_id").agg(

        total_received=("received_quantity", "sum"),

        total_shipments=("shipment_id", "count")

    ).reset_index()

    print("--------------------------------------")
    print("Inventory Summary")
    print("--------------------------------------")
    print(inventory.head())

    return inventory


# ============================================================
# Save Gold Files
# ============================================================

def save_gold_files(
    ghost,
    phantom,
    mismatch,
    delayed,
    scorecard,
    inventory,
    gold_path
):

    ghost.to_csv(
        os.path.join(gold_path, "ghost_shipments.csv"),
        index=False
    )

    phantom.to_csv(
        os.path.join(gold_path, "phantom_receipts.csv"),
        index=False
    )

    mismatch.to_csv(
        os.path.join(gold_path, "quantity_mismatch.csv"),
        index=False
    )

    delayed.to_csv(
        os.path.join(gold_path, "delivery_delay.csv"),
        index=False
    )
     
    scorecard.to_csv(
        os.path.join(gold_path, "supplier_scorecard.csv"),
        index=False
    )


    inventory.to_csv(
    os.path.join(
        gold_path,
        "inventory_summary.csv"
    ),
    index=False
)

    print("\nGold Files Saved Successfully")


# ============================================================
# Main Function
# ============================================================

def main():

    print("=" * 60)
    print("Starting Gold Layer Analytics")
    print("=" * 60)

    # Load Config
    config = load_config()

    # Read Silver Data
    shipments, receipts, suppliers, products = load_silver_data(config)

    # Create Gold Folder
    gold_path = create_gold_folder(config)

    # Analytics
    ghost = detect_ghost_shipments(shipments, receipts)

    phantom = detect_phantom_receipts(shipments, receipts)

    mismatch = detect_quantity_mismatch(shipments, receipts)

    delayed = detect_delivery_delay(shipments, receipts)

    scorecard = create_supplier_scorecard(
        shipments,
        delayed
    )
    inventory = create_inventory_summary(receipts)

    # Save Output
    save_gold_files(
        ghost,
        phantom,
        mismatch,
        delayed,
        scorecard,
        inventory,
        gold_path
    )

    print("\n")
    print("=" * 60)
    print("Gold Layer Completed Successfully")
    print("=" * 60)


if __name__ == "__main__":
    main()