# 🚀 Customer Sales Insights Using SQL

> Advanced SQL Analysis of the Superstore Dataset using Subqueries, CTEs, Window Functions, Ranking Techniques, and Business Intelligence Reporting.

---

## 📖 Overview

This project demonstrates the practical application of advanced SQL concepts to analyze customer sales data and generate meaningful business insights.

Using the Superstore Dataset, customer transactions were analyzed to identify revenue-generating customers, purchasing patterns, sales trends, and customer rankings. The project focuses on transforming raw sales data into actionable information that can support business decision-making.

---

## 🎯 Business Objective

The primary goals of this analysis are:

✔ Identify high-value customers

✔ Analyze customer purchasing behavior

✔ Rank customers based on revenue contribution

✔ Detect top-performing and low-performing customers

✔ Generate customer-centric business insights

✔ Apply advanced SQL concepts in a real-world scenario

---

## 📊 Dataset Description

The analysis is performed on the **Superstore Sales Dataset**, which contains transactional records related to:

- Customers
- Orders
- Products
- Sales
- Profit
- Categories
- Regions
- Shipping Information

The dataset provides a realistic business environment for performing analytical SQL operations and customer segmentation.

---

## 🏗 Data Preparation

To improve data organization and analytical efficiency, the raw dataset was normalized into separate logical entities:

### 👥 Customers

Contains customer-specific information.

- Customer ID
- Customer Name
- Segment

### 🛒 Orders

Contains transaction-level details.

- Order ID
- Order Date
- Customer ID
- Sales
- Profit

### 📦 Products

Contains product-related information.

- Product ID
- Category
- Sub-Category
- Product Name

---

## 🧠 SQL Concepts Implemented

### 🔹 Subqueries

Used for comparative analysis and filtering records using aggregated values.

### 🔹 Correlated Subqueries

Used to identify the highest-value order for each customer.

### 🔹 Common Table Expressions (CTEs)

Used to simplify complex calculations and improve query readability.

### 🔹 Window Functions

Used for advanced analytical reporting and customer ranking.

### 🔹 Ranking Functions

Implemented using:

- RANK()
- ROW_NUMBER()

### 🔹 JOIN Operations

Used to combine customer and sales information into a consolidated report.

---

## 📌 Analytical Tasks Performed

### Q1. Orders Above Average Sales

Identified all orders where sales exceeded the overall average sales value.

### Q2. Highest Sales Order for Each Customer

Determined the maximum-value order placed by every customer.

### Q3. Total Sales Per Customer

Calculated customer-wise revenue contribution using Common Table Expressions.

### Q4. Customers with Above-Average Sales

Identified customers generating revenue above the average customer level.

### Q5. Customer Ranking Analysis

Ranked customers according to total sales generated.

### Q6. Order Ranking Within Customer Groups

Assigned row numbers to customer orders using PARTITION BY and ROW_NUMBER().

### Q7. Top 3 Customers

Identified the highest-performing customers based on total revenue.

---

## 📈 Mini Project: Customer Sales Insights

### 🥇 Top 5 Customers

Identified customers contributing the highest sales revenue.

### 📉 Bottom 5 Customers

Identified customers with the lowest revenue contribution.

### 👤 Single Order Customers

Detected customers who placed only one order.

### 📊 Above Average Customers

Analyzed customers whose sales exceeded average customer sales.

### 💰 Highest Order Value Per Customer

Evaluated the maximum spending capacity of individual customers.

---

## 💡 Key Business Insights

🔹 A small percentage of customers contribute a large share of overall revenue.

🔹 Customer ranking enables effective customer segmentation.

🔹 High-value customers can be targeted through loyalty and retention programs.

🔹 Single-order customers represent potential opportunities for customer engagement.

🔹 Sales analysis helps organizations prioritize customer relationships and improve business performance.

🔹 Revenue-based customer analysis supports data-driven strategic decision-making.

---

## 🛠 Tools & Technologies

| Technology | Purpose |
|------------|----------|
| MySQL 8.0 | Database Management |
| SQL | Data Analysis |
| MySQL Workbench | Query Development |
| GitHub | Version Control & Documentation |

---

## 🎓 Learning Outcomes

Through this project, the following skills were strengthened:

- Advanced SQL Query Writing
- Business Data Analysis
- Customer Segmentation
- Window Functions
- Ranking Techniques
- Data Aggregation
- Business Intelligence Reporting
- Real-World SQL Problem Solving

---

## 📋 Conclusion

This project demonstrates how advanced SQL techniques can be leveraged to extract valuable business insights from transactional datasets.

By implementing Subqueries, Correlated Subqueries, Common Table Expressions (CTEs), Window Functions, Ranking Functions, and JOIN operations, meaningful customer-centric analysis was performed to evaluate sales performance and customer behavior.

The project highlights the importance of SQL in modern business analytics and showcases its ability to support data-driven decision-making processes.

---

## 👨‍💻 Author

**Priyanshu Tiwari**

B.Tech Computer Science Engineering

SQL • Data Analytics • Business Intelligence • Problem Solving

**Celebal Technologies Summer Internship Program 2026**
