# Question-wise Implementation Summary

## Q1. Limitations of MapReduce

### Objective
Understand why Apache Spark is preferred over traditional MapReduce.

### Concepts Used
- In-Memory Computing
- Distributed Processing

### Solution Approach
Studied the limitations of MapReduce such as high disk I/O, slower iterative processing, and complex programming. Compared these limitations with Spark's in-memory processing capabilities.

---

## Q2. In-Memory Computing

### Objective
Understand how Spark improves performance.

### Concepts Used
- Memory Caching
- Distributed Computing

### Solution Approach
Explained how Spark stores intermediate data in memory instead of repeatedly reading and writing data to disk, reducing execution time for iterative workloads.

---

## Q3. Remove Duplicate Rows

### Objective
Remove duplicate records using specific columns.

### Concepts Used
- Data Cleaning
- dropDuplicates()

### Solution Approach
Used dropDuplicates() on user_id and transaction_date to ensure each transaction record remained unique.

---

## Q4. Filter and Aggregate Data

### Objective
Find average sales by product category for the West region.

### Concepts Used
- filter()
- groupBy()
- avg()

### Solution Approach
Filtered records where region equals West and grouped data by product category to calculate average sales amount.

---

## Q5. Handle Null Values

### Objective
Understand different null handling techniques.

### Concepts Used
- na.drop()
- na.fill()

### Solution Approach
Compared row removal and value replacement approaches. Filled missing status values with "Unknown" to improve data consistency.

---

## Q6. City-wise Record Count

### Objective
Find cities having more than 100 records.

### Concepts Used
- groupBy()
- count()
- filter()

### Solution Approach
Grouped records by city, calculated counts, and filtered cities whose count exceeded 100.

---

## Q7. DataFrame Immutability

### Objective
Understand Spark DataFrame behavior.

### Concepts Used
- Immutable DataFrames

### Solution Approach
Studied how transformations create new DataFrames rather than modifying the existing dataset.

---

## Q8. Multi-condition Filtering

### Objective
Filter Premium users aged between 18 and 30.

### Concepts Used
- between()
- Logical Conditions

### Solution Approach
Applied multiple filter conditions to retrieve the required customer segment.

---

## Q9. Null Handling Before Aggregation

### Objective
Understand data quality requirements.

### Concepts Used
- Data Cleaning
- Aggregation Best Practices

### Solution Approach
Explained how missing values can impact calculations and why they should be addressed before aggregation.

---

## Q10. Data Type Conversion

### Objective
Convert timestamp column into TimestampType.

### Concepts Used
- cast()
- TimestampType

### Solution Approach
Converted raw timestamp data into a Spark timestamp format and renamed the column to event_time.

---

## Q11. Shuffle Operation

### Objective
Understand Spark execution behavior.

### Concepts Used
- Shuffle
- Wide Transformations

### Solution Approach
Studied how Spark redistributes data across partitions during GroupBy and aggregation operations.

---

## Q12. Invalid Record Removal

### Objective
Remove incomplete records.

### Concepts Used
- filter()
- isNotNull()

### Solution Approach
Removed records where email was null or username was empty to improve dataset quality.

---

## Q13. Multiple Aggregations

### Objective
Calculate multiple statistics simultaneously.

### Concepts Used
- agg()
- min()
- max()
- avg()

### Solution Approach
Used a single aggregation query to generate minimum, maximum, and average values for sale_amount.

---

## Q14. Schema Inference Risks

### Objective
Understand challenges of automatic schema detection.

### Concepts Used
- inferSchema

### Solution Approach
Explained how inconsistent date formats can lead to incorrect data type detection and parsing issues.

---

## Q15. ETL Processing Pipeline

### Objective
Build a complete processing workflow.

### Concepts Used
- dropDuplicates()
- na.fill()
- groupBy()
- sum()

### Solution Approach
Developed an end-to-end ETL pipeline that removed duplicates, handled missing prices, grouped data by store_id, and calculated total revenue for each store.

---

# Overall Learning

This assignment provided hands-on experience with Apache Spark DataFrames and demonstrated how data cleaning, transformation, filtering, aggregation, and ETL operations are performed in real-world data engineering workflows. The implementation improved understanding of distributed data processing, data quality management, and analytical reporting using Spark.
