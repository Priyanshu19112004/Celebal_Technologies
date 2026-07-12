# 🚚 Supply Chain Delay & Inventory Mismatch Detector

## 📌 Project Overview

The **Supply Chain Delay & Inventory Mismatch Detector** is an end-to-end data engineering project that simulates a modern supply chain data pipeline using a multi-layer architecture (Raw → Bronze → Silver → Gold).

The project ingests raw supplier and warehouse datasets, performs data validation and transformation, detects supply chain anomalies, and generates analytics-ready datasets for reporting and business intelligence.

---

# 🎯 Project Objectives

- Build an end-to-end ETL pipeline using Python.
- Implement Medallion Architecture (Bronze, Silver, Gold).
- Validate and clean supply chain data.
- Detect shipment delays and inventory mismatches.
- Generate supplier performance metrics.
- Create analytics-ready datasets for dashboards.

---

# 🏗 Project Architecture

```
Raw Data
    │
    ▼
Bronze Layer
(Data Ingestion & Audit Columns)
    │
    ▼
Silver Layer
(Data Cleaning & Validation)
    │
    ▼
Gold Layer
(Business Analytics)
    │
    ▼
Dashboard / Reporting
```

---

# 📂 Project Structure

```
Supply_Chain_Delay_Inventory_Detector

│
├── config
│   └── pipeline_config.json
│
├── data
│   ├── raw
│   ├── bronze
│   ├── silver
│   ├── gold
│   └── quarantine
│
├── scripts
│   ├── 01_bronze_ingestion.py
│   ├── 02_silver_transform.py
│   └── 03_gold_analytics.py
│
├── dashboard
├── reports
├── screenshots
│
├── requirements.txt
└── README.md
```

---

# ⚙ Technologies Used

- Python
- Pandas
- NumPy
- JSON
- OpenPyXL
- PyArrow
- Matplotlib
- Faker
- VS Code

---

# 📌 Pipeline Stages

## Bronze Layer

- Reads raw CSV datasets
- Adds audit columns
- Preserves original data
- Stores data into Bronze layer

### Audit Columns Added

- ingested_at
- source_file
- pipeline_version

---

## Silver Layer

Data Quality Rules

- Missing Value Validation
- Duplicate Removal
- Date Standardization
- Quantity Validation
- Invalid Record Detection
- Quarantine Management

Output

- Clean Silver datasets
- Invalid records moved to Quarantine

---

## Gold Layer

Business Analytics

- Ghost Shipment Detection
- Phantom Receipt Detection
- Quantity Mismatch Detection
- Delivery Delay Detection
- Supplier Scorecard
- Inventory Summary

---

# 📊 Output Files

Gold Layer generates

- ghost_shipments.csv
- phantom_receipts.csv
- quantity_mismatch.csv
- delivery_delay.csv
- supplier_scorecard.csv
- inventory_summary.csv

---

# 📈 Business Insights

The project helps identify

- Delayed Shipments
- Supplier Performance
- Inventory Flow
- Shipment Tracking
- Warehouse Performance
- Supply Chain Bottlenecks

---

# ▶ How to Run

Install dependencies

```bash
pip install -r requirements.txt
```

Run Bronze Layer

```bash
python scripts/01_bronze_ingestion.py
```

Run Silver Layer

```bash
python scripts/02_silver_transform.py
```

Run Gold Layer

```bash
python scripts/03_gold_analytics.py
```

---

# 📊 Future Improvements

- Power BI Dashboard
- Apache Airflow Scheduling
- Azure Data Factory Integration
- SQL Data Warehouse
- Email Alerts
- Cloud Deployment

---

# 👨‍💻 Author

**Priyanshu Tiwari**

Data Engineering Project

Built for learning modern ETL pipeline architecture and supply chain analytics.