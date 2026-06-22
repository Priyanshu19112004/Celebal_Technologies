# Week 5 – Apache Spark Data Processing Assignment

## Objective

The objective of this assignment is to understand and implement Apache Spark DataFrame operations for data cleaning, transformation, filtering, aggregation, and analytical processing.

The assignment focuses on applying Spark concepts to a structured dataset while demonstrating practical data engineering techniques used in real-world data processing workflows.

---

## Technologies Used

- Apache Spark
- PySpark
- Python
- Google Colab

---

## Dataset

A synthetic dataset containing customer transaction information was created for this assignment.

The dataset includes:

- User Information
- Transaction Details
- Product Categories
- Regional Data
- Subscription Information
- Missing Values
- Duplicate Records

This allowed the implementation of various data cleaning and transformation techniques.

---

## Tasks Performed

### Q1 – Spark vs MapReduce

Studied the limitations of traditional MapReduce and understood how Apache Spark provides faster processing through in-memory computation.

### Q2 – In-Memory Computing

Explored Spark's ability to store intermediate data in memory, improving performance for iterative computations.

### Q3 – Duplicate Removal

Removed duplicate records using selected columns:

- user_id
- transaction_date

### Q4 – Filtering and Aggregation

Filtered records for the West region and calculated average sales by product category.

### Q5 – Null Value Handling

Implemented:

- `.na.drop()`
- `.na.fill()`

to manage missing data effectively.

### Q6 – Grouping Operations

Calculated city-wise record counts and filtered cities with more than 100 records.

### Q7 – DataFrame Immutability

Understood how Spark DataFrames create new DataFrames after transformations instead of modifying existing data.

### Q8 – Conditional Filtering

Filtered customers aged between 18 and 30 with Premium subscriptions.

### Q9 – Data Cleaning Best Practices

Learned the importance of handling null values before performing aggregations.

### Q10 – Data Type Conversion

Converted timestamp columns into Spark TimestampType format.

### Q11 – Shuffle Operations

Studied the concept of shuffle and its role in wide transformations.

### Q12 – Invalid Record Removal

Removed records containing null emails or empty usernames.

### Q13 – Multiple Aggregations

Calculated minimum, maximum, and average sales values using aggregation functions.

### Q14 – Schema Inference Risks

Understood challenges associated with inferSchema when working with inconsistent source data.

### Q15 – ETL Processing Pipeline

Built a complete processing workflow involving:

- Duplicate Removal
- Null Handling
- Grouping
- Revenue Aggregation

---

## Spark Concepts Covered

- SparkSession
- DataFrames
- Data Cleaning
- Null Handling
- Duplicate Removal
- Filtering
- Aggregation Functions
- GroupBy Operations
- Data Type Casting
- Shuffle Operations
- ETL Processing

---

## Key Learning Outcomes

Through this assignment, I gained hands-on experience with Apache Spark DataFrames and learned how to perform data cleaning, transformation, aggregation, and analytical operations efficiently.

The assignment helped strengthen my understanding of distributed data processing concepts, Spark transformations, and ETL workflows commonly used in modern data engineering environments.

---

## Conclusion

This assignment successfully demonstrates the practical application of Apache Spark for processing and analyzing structured data. By implementing data cleaning, transformation, filtering, and aggregation techniques, a complete data processing workflow was developed using PySpark DataFrames.

---

## Author

**Priyanshu Tiwari**

B.Tech Computer Science Engineering

Celebal Technologies Internship Program
