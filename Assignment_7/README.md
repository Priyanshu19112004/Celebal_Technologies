# Delta Lake Incremental Data Processing Assignment

## 📌 Objective

The objective of this assignment is to perform incremental data processing using Delta Lake in Databricks. The assignment demonstrates how to load data into a Delta Table, clean the data, create incremental records, apply the MERGE operation, validate the results, and generate summary statistics.

---

## 🛠️ Tools & Technologies

- Databricks Free Edition
- Apache Spark (PySpark)
- Delta Lake
- Python

---

## 📂 Dataset

- **Master Dataset:** Sample - Superstore.csv
- **Incremental Dataset:** customer_incremental.csv

---

## 🚀 Steps Performed

### Step 1: Load Dataset into a Delta Table
- Loaded the Superstore dataset into a Spark DataFrame.
- Verified the schema and total row count.
- Renamed column names by replacing spaces with underscores.
- Stored the dataset as a Delta Table (`superstore_delta`).

### Step 2: Perform Basic Cleaning
- Checked for null values.
- Removed duplicate records using `dropDuplicates()`.
- Replaced null values in numeric columns using `fillna()`.

### Step 3: Create Incremental Dataset
- Selected existing records and modified them to simulate updates.
- Created new records by assigning new `Row_ID` values.
- Combined updated and new records into a single incremental dataset.

### Step 4: Apply MERGE Operation
- Loaded the Delta Table using the DeltaTable API.
- Applied the MERGE operation using `Row_ID` as the matching key.
- Updated existing records and inserted new records.

### Step 5: Validate Results
- Verified the final row count.
- Checked for duplicate records based on `Row_ID`.
- Confirmed that no duplicate records were present after the MERGE operation.

### Step 6: Display Final Dataset and Summary
- Displayed the final Delta Table.
- Generated summary statistics including total orders, total sales, total profit, and average discount.

---

## 📁 Project Structure

```text
delta-lake-assignment/
│
├── data/
│   ├── Sample - Superstore.csv
│   └── customer_incremental.csv
│
├── notebooks/
│   └── delta_lake_assignment.ipynb
│
├── screenshots/
│   ├── step1_load_dataset.png
│   ├── step2_data_cleaning.png
│   ├── step3_incremental_dataset.png
│   ├── step4_merge_operation.png
│   ├── step5_validation.png
│   └── step6_final_summary.png
│
└── README.md
```

---

## ✅ Output

- Delta Table created successfully.
- Data cleaned by handling null values and removing duplicate records.
- Incremental dataset created successfully.
- MERGE operation completed successfully.
- Validation confirmed that no duplicate records were present.
- Final dataset and summary statistics were generated successfully.

---
