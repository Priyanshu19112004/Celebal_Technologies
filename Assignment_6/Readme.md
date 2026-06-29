# Week 6 – Apache Spark Assignment

## Overview

This repository contains the implementation of Week 6 Apache Spark Assignment using **PySpark**, focusing on distributed data processing, Spark DataFrame operations, schema management, and performance optimization techniques. The assignment combines practical data engineering tasks with core Spark concepts to build a strong foundation in large-scale data processing.

The project is divided into:

- **Part 1:** Employee Data Processing using PySpark
- **Part 2:** Spark Architecture & Advanced DataFrame Operations

---

## Assignment Objectives

- Understand Apache Spark Architecture and execution model
- Explore Driver, Executors, and Cluster Manager components
- Learn Lazy Evaluation and DAG-based execution
- Process structured data using Spark DataFrames
- Perform filtering, transformations, and aggregations
- Handle schema inference and data type conversions
- Manage missing values efficiently
- Build reusable Spark data processing pipelines
- Compare CSV and Parquet storage formats
- Apply Spark performance optimization techniques

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| PySpark | Distributed Data Processing |
| Apache Spark | Big Data Framework |
| Jupyter Notebook / Google Colab | Development Environment |
| CSV | Source Data Format |
| Parquet | Optimized Storage Format |

---

# Part 1: Employee Data Processing Pipeline

### Key Implementations

- SparkSession Initialization
- CSV Data Ingestion
- Schema Inference & Validation
- Data Exploration using DataFrames
- Column Selection & Filtering
- Data Type Casting
- Column Renaming
- Derived Column Creation
- NULL Value Handling
- Data Processing Pipeline Construction
- Data Export in CSV Format
- Data Export in Parquet Format

### Skills Demonstrated

- ETL Workflow Development
- Data Cleaning & Transformation
- Schema Management
- Spark DataFrame API Usage
- Distributed Data Processing

---

# Part 2: Apache Spark Concepts & Optimization

### Topics Covered

#### Spark Architecture
Understanding the interaction between:

- Driver Program
- Cluster Manager
- Worker Nodes
- Executors

#### Lazy Evaluation
Spark delays execution until an action is triggered, enabling query optimization and reduced resource consumption.

#### DAG (Directed Acyclic Graph)
Spark creates a lineage graph to optimize execution plans and provide fault tolerance during distributed processing.

#### Predicate Pushdown
Filters are pushed closer to the data source, minimizing unnecessary data scans and improving query performance.

#### Transformations vs Actions

| Transformations | Actions |
|---------------|----------|
| filter() | show() |
| select() | collect() |
| withColumn() | count() |
| drop() | take() |

#### CSV vs Parquet Comparison

| Feature | CSV | Parquet |
|----------|------|----------|
| Storage Type | Row-Based | Columnar |
| Compression | Low | High |
| Query Performance | Moderate | Fast |
| Schema Support | Limited | Strong |
| Analytics Workloads | Less Efficient | Highly Optimized |

---

# Performance Optimization Insights

### Optimization Techniques Applied

- Leveraged Spark's Lazy Evaluation model
- Reduced data movement across executors
- Selected only required columns
- Used efficient column transformations
- Stored processed datasets in Parquet format
- Avoided unnecessary Driver memory usage

### Best Practices Followed

- Prefer `show()` over `collect()` for data inspection
- Use schema inference carefully for large datasets
- Filter data as early as possible
- Persist only when required
- Store analytical datasets in Parquet format
- Minimize wide transformations when possible

---

# Key Learning Outcomes

Through this assignment, the following competencies were developed:

- Apache Spark Fundamentals
- Distributed Computing Concepts
- Spark DataFrame Operations
- Schema Handling & Data Validation
- ETL Pipeline Development
- Performance Optimization Strategies
- Fault Tolerance using DAG
- Predicate Pushdown Optimization
- Storage Format Evaluation
- Big Data Processing Best Practices

---

# Business Relevance

Apache Spark is widely used in modern Data Engineering and Analytics platforms for processing large-scale datasets. The concepts implemented in this assignment directly align with real-world industry use cases such as:

- Data Pipeline Development
- ETL & ELT Workflows
- Data Lake Processing
- Cloud-Based Analytics
- Batch Data Processing
- Big Data Engineering

---

# Conclusion

This assignment demonstrates the practical application of Apache Spark for scalable data processing and analytics. By implementing DataFrame transformations, schema management, lazy evaluation, DAG-based execution, and storage optimization through Parquet, the project showcases essential Data Engineering skills required for handling large-scale data workloads in enterprise environments.

The assignment strengthens foundational knowledge of Spark while introducing industry-relevant optimization techniques used in modern Big Data ecosystems.
