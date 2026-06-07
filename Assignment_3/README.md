# Customer Sales Insights Using SQL

## Overview

This assignment demonstrates the use of advanced SQL concepts to analyze customer sales data from the Superstore dataset. The project focuses on extracting meaningful business insights using Subqueries, Common Table Expressions (CTEs), Window Functions, and JOIN operations.

The objective is to identify high-value customers, analyze purchasing behavior, rank customers based on revenue contribution, and generate analytical reports that support business decision-making.

---

## Dataset Information

**Dataset:** Sample Superstore Dataset

The dataset contains information related to:

- Customer Details
- Orders
- Products
- Sales
- Profit
- Category
- Region
- Shipping Information

---

## Database Schema

The raw dataset was normalized into the following tables:

### Customers

Stores unique customer information.

| Column |
|----------|
| Customer ID |
| Customer Name |
| Segment |

### Orders

Stores sales transaction details.

| Column |
|----------|
| Order ID |
| Order Date |
| Customer ID |
| Sales |
| Profit |

### Products

Stores product information.

| Column |
|----------|
| Product ID |
| Category |
| Sub-Category |
| Product Name |

---

## SQL Concepts Implemented

### Subqueries

- Orders with sales greater than average sales
- Highest sales order for each customer

### Common Table Expressions (CTEs)

- Customer-wise sales calculation
- Above-average customer identification

### Window Functions

- Customer ranking using RANK()
- Order ranking using ROW_NUMBER()
- Top customer identification

### JOIN Operations

- Customer performance report generation

---

## Assignment Tasks

### Q1
Find all orders where sales are greater than average sales.

### Q2
Find the highest sales order for each customer.

### Q3
Calculate total sales for each customer using a CTE.

### Q4
Find customers whose total sales are above average.

### Q5
Rank all customers based on total sales.

### Q6
Assign row numbers to each order within a customer using PARTITION BY.

### Q7
Display the top 3 customers based on total sales.

---

## Final Business Analysis Query

Generated a consolidated customer performance report displaying:

- Customer Name
- Total Sales
- Customer Rank

Concepts Used:

- CTE
- JOIN
- Window Function

---

## Mini Project

### Customer Sales Insights

- Top 5 Customers
- Bottom 5 Customers
- Customers Who Made Only One Order
- Customers Having Above-Average Sales
- Highest Order Value Per Customer

---

## Key Business Insights

- Top customers contribute a major share of total revenue.
- Customer ranking helps identify high-value customers.
- Above-average customers can be targeted through loyalty programs.
- Single-order customers may require retention strategies.
- Maximum order value analysis helps understand customer purchasing behavior.

---

## Technologies Used

- MySQL 8.0
- SQL
- MySQL Workbench

---

## Project Structure

```text
Customer_Sales_Insights_SQL
│
├── Dataset
│   └── Superstore_raw.csv
│
├── SQL
│   └── Assignment_3.sql
│
├── Screenshots
│   ├── Q1_Output.png
│   ├── Q2_Output.png
│   ├── ...
│
├── Assignment_3_Report.docx
│
└── README.md
```

---

## Conclusion

This project demonstrates the practical implementation of SQL analytical techniques for business reporting and customer analysis. By leveraging Subqueries, CTEs, Window Functions, and JOIN operations, meaningful insights were extracted from the Superstore dataset, enabling data-driven decision-making and customer performance evaluation.

---

### Author

**Priyanshu Tiwari**  
B.Tech CSE  
Celebal Technologies Summer Internship 2026
