# Customer Data Processing Pipeline using Apache Spark

## Overview

This project demonstrates the implementation of a scalable data processing pipeline using Apache Spark DataFrames. The workflow covers data ingestion, cleaning, transformation, filtering, aggregation, and reporting operations commonly used in Data Engineering and Big Data environments.

The project was developed as part of the Celebal Technologies Internship Program to gain hands-on experience with distributed data processing using PySpark.

---

## Project Objectives

- Understand Apache Spark architecture and DataFrame APIs
- Perform data cleaning and preprocessing
- Handle missing and duplicate records
- Apply schema transformations
- Perform filtering and business rule implementation
- Generate aggregated insights using Spark functions
- Execute GroupBy and Pivot transformations
- Build an end-to-end ETL workflow

---

## Technologies Used

- Apache Spark
- PySpark
- Python
- Google Colab
- Jupyter Notebook

---

## Dataset Description

A synthetic customer dataset was created to simulate real-world business scenarios.

### Dataset Attributes

| Column | Description |
|----------|-------------|
| Customer_ID | Unique customer identifier |
| Name | Customer name |
| Age | Customer age |
| Region | Customer region |
| Monthly_Income | Monthly income |
| Gender | Customer gender |

The dataset intentionally includes:
- Missing values
- Duplicate records
- Inconsistent entries

to demonstrate practical data-cleaning techniques.

---

## Project Workflow

### 1. Data Ingestion

- Created Spark Session
- Loaded customer dataset into Spark DataFrame

### 2. Data Exploration

- Displayed sample records
- Inspected schema structure
- Counted total records

### 3. Data Cleaning

- Identified null values
- Replaced missing data with default values
- Removed duplicate records

### 4. Data Transformation

- Renamed columns
- Created derived business attributes
- Categorized customers based on income

### 5. Data Filtering

- Selected customers above specific age thresholds
- Identified high-income customers

### 6. Aggregation Analysis

Calculated:

- Total Customers
- Total Income
- Average Income
- Minimum Income
- Maximum Income

### 7. GroupBy Analysis

Generated region-wise analysis including:

- Customer Count
- Average Income
- Total Income

### 8. Pivot Transformation

Performed gender-wise income analysis using Spark Pivot operations.

### 9. ETL Pipeline

Built an end-to-end ETL workflow integrating:

- Data Cleaning
- Data Transformation
- Aggregation
- Business Reporting

---

## Key Spark Concepts Implemented

- SparkSession
- DataFrames
- Schema Management
- Null Handling
- Duplicate Removal
- Column Transformation
- Filtering Operations
- Aggregation Functions
- GroupBy Operations
- Pivot Transformations
- ETL Pipeline Development

---

## Sample Business Insights

- North region generated the highest total revenue.
- East region showed the highest average income.
- Data quality improved significantly after cleaning operations.
- Gender-wise income distribution was analyzed using pivot transformations.
- Spark DataFrames enabled efficient analytical processing.

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Distributed data processing
- Data cleaning and preparation
- Spark DataFrame transformations
- Aggregation and reporting
- ETL pipeline development
- Big Data analytics workflows

---

## Future Enhancements

- Process larger datasets from external storage
- Integrate Spark SQL for advanced analytics
- Connect with cloud storage platforms
- Build automated data pipelines using orchestration tools

---

## Author

**Priyanshu Tiwari**

B.Tech Computer Science Engineering

Celebal Technologies Internship Program

Apache Spark | Data Engineering | Big Data Analytics
