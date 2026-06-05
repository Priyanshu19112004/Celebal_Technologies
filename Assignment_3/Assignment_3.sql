-- =====================================================
-- CELEBAL SUMMER INTERNSHIP 2026
-- WEEK 3 TASK : CUSTOMER SALES INSIGHTS
-- Assignment_3.sql
-- =====================================================

USE superstore_db;

-- =====================================================
-- SECTION A : DATA PREPARATION
-- =====================================================

-- Create Customers Table

CREATE TABLE customers AS
SELECT DISTINCT
    `Customer ID`,
    `Customer Name`,
    Segment
FROM superstore_raw;

-- Output:
-- Customers table created successfully.

---------------------------------------------------------

-- Create Orders Table

CREATE TABLE orders AS
SELECT DISTINCT
    `Order ID`,
    `Order Date`,
    `Customer ID`,
    Sales,
    Profit
FROM superstore_raw;

-- Output:
-- Orders table created successfully.

---------------------------------------------------------

-- Create Products Table

CREATE TABLE products AS
SELECT DISTINCT
    `Product ID`,
    Category,
    `Sub-Category`,
    `Product Name`
FROM superstore_raw;

-- Output:
-- Products table created successfully.



-- =============================================================
-- Q1. Find Orders with Sales Greater than Average Sales
-- Concept Used : Subquery
-- =============================================================

SELECT *
FROM orders
WHERE Sales >
(
    SELECT AVG(Sales)
    FROM orders
);

-- Output:
-- Orders having sales above average displayed.

-- Business Insight:
-- These orders represent higher-value transactions
-- and contribute significantly to overall revenue.



-- =============================================================
-- Q2. Highest Sales Order for Each Customer
-- Concept Used : Correlated Subquery
-- =============================================================

SELECT *
FROM orders o
WHERE Sales =
(
    SELECT MAX(Sales)
    FROM orders
    WHERE `Customer ID` = o.`Customer ID`
);

-- Output:
-- Highest-value order identified for each customer.

-- Business Insight:
-- Helps identify peak purchasing behaviour
-- of individual customers.


-- =============================================================
-- Q3. Calculate Total Sales Per Customer
-- Concept Used : Common Table Expression (CTE)
-- =============================================================

WITH customer_sales AS
(
    SELECT
        `Customer ID`,
        SUM(Sales) AS Total_Sales
    FROM orders
    GROUP BY `Customer ID`
)

SELECT *
FROM customer_sales;

-- Output:
-- Total sales calculated for all customers.

-- Business Insight:
-- Provides customer-wise revenue contribution.


-- =============================================================
-- Q4. Find Customers Whose Total Sales are Above Average
-- Concept Used : CTE + Subquery
-- =============================================================

WITH customer_sales AS
(
    SELECT
        `Customer ID`,
        SUM(Sales) AS Total_Sales
    FROM orders
    GROUP BY `Customer ID`
)

SELECT *
FROM customer_sales
WHERE Total_Sales >
(
    SELECT AVG(Total_Sales)
    FROM customer_sales
);

-- Output:
-- Customers having total sales above average displayed.

-- Business Insight:
-- These customers contribute significantly more
-- revenue than the average customer and can be
-- considered high-value customers.


-- =============================================================
-- Q5. Rank Customers by Total Sales
-- Concept Used : Window Function (RANK)
-- =============================================================

WITH customer_sales AS
(
    SELECT
        `Customer ID`,
        SUM(Sales) AS Total_Sales
    FROM orders
    GROUP BY `Customer ID`
)

SELECT
    `Customer ID`,
    Total_Sales,

    RANK() OVER
    (
        ORDER BY Total_Sales DESC
    ) AS Sales_Rank
FROM customer_sales;

-- Output:
-- Customer ranking generated successfully.

-- Business Insight:
-- Rank 1 customer generated the highest revenue.
-- Useful for loyalty and retention programs.


-- =============================================================
-- FINAL BUSINESS ANALYSIS QUERY
-- Concepts Used:
-- 1. CTE
-- 2. JOIN
-- 3. Window Function
-- =============================================================

WITH customer_sales AS
(
    SELECT
        `Customer ID`,
        SUM(Sales) AS Total_Sales
    FROM orders
    GROUP BY `Customer ID`
)

SELECT
    c.`Customer Name`,
    cs.Total_Sales,

    RANK() OVER
    (
        ORDER BY cs.Total_Sales DESC
    ) AS Customer_Rank

FROM customer_sales cs
JOIN customers c
ON cs.`Customer ID` = c.`Customer ID`;

-- Output:
-- Customer Name, Total Sales and Rank displayed.

-- Business Insight:
-- Provides a consolidated customer performance report.
-- Enables identification of top-performing customers.


-- =============================================================
-- MP1. Top 5 Customers by Total Sales
-- =============================================================

SELECT
    `Customer ID`,
    SUM(Sales) AS Total_Sales
FROM orders
GROUP BY `Customer ID`
ORDER BY Total_Sales DESC
LIMIT 5;

-- Output:
-- Top 5 customers displayed.

-- Business Insight:
-- These customers contribute the highest revenue.



-- =============================================================
-- MP2. Bottom 5 Customers by Total Sales
-- =============================================================

SELECT
    `Customer ID`,
    SUM(Sales) AS Total_Sales
FROM orders
GROUP BY `Customer ID`
ORDER BY Total_Sales ASC
LIMIT 5;

-- Output:
-- Bottom 5 customers displayed.

-- Business Insight:
-- These customers have the lowest sales contribution.



-- =============================================================
-- MP3. Customers Who Made Only One Order
-- =============================================================

SELECT
    `Customer ID`,
    COUNT(`Order ID`) AS Total_Orders
FROM orders
GROUP BY `Customer ID`
HAVING COUNT(`Order ID`) = 1;

-- Output:
-- Customers with exactly one order displayed.

-- Business Insight:
-- These customers may require retention efforts.



-- =============================================================
-- MP4. Customers Having Above-Average Sales
-- =============================================================

WITH customer_sales AS
(
    SELECT
        `Customer ID`,
        SUM(Sales) AS Total_Sales
    FROM orders
    GROUP BY `Customer ID`
)

SELECT *
FROM customer_sales
WHERE Total_Sales >
(
    SELECT AVG(Total_Sales)
    FROM customer_sales
);



-- =============================================================
-- MP5. Highest Order Value Per Customer
-- =============================================================

SELECT
    `Customer ID`,
    MAX(Sales) AS Highest_Order_Value
FROM orders
GROUP BY `Customer ID`
ORDER BY Highest_Order_Value DESC;

-- Output:
-- Highest order value identified for each customer.

-- Business Insight:
-- Reveals the maximum spending capacity of customers.

-- Output:
-- Above-average customers displayed.

-- Business Insight:
-- These customers are key contributors to revenue.



-- =============================================================
-- CELEBAL TECHNOLOGIES
-- Summer Internship Program 2026
-- Week 3 Assignment
-- Customer Sales Insights Using SQL
--
-- Name : Priyanshu Tiwari
-- Technology : MySQL
-- Dataset : Sample Superstore Dataset
-- =============================================================


-- =============================================================
-- SECTION A : DATA PREPARATION
-- =============================================================

-- Create Customers Table

-- Create Orders Table

-- Create Products Table


-- =============================================================
-- SECTION B : REQUIRED QUERIES
-- =============================================================

-- Q1. Find all orders where sales are greater than the average sales.
-- Concept Used: Subquery

-- Q2. Find the highest sales order for each customer.
-- Concept Used: Correlated Subquery

-- Q3. Calculate total sales for each customer.
-- Concept Used: Common Table Expression (CTE)

-- Q4. Find customers whose total sales are above average.
-- Concept Used: CTE + Subquery

-- Q5. Rank all customers based on total sales.
-- Concept Used: Window Function (RANK)

-- Q6. Assign row numbers to each order within a customer.
-- Concept Used: Window Function (ROW_NUMBER)

-- Q7. Display top 3 customers based on total sales.
-- Concept Used: Window Function (RANK)


-- =============================================================
-- SECTION C : FINAL COMBINED QUERY
-- =============================================================

-- Generate a report showing:
-- Customer Name
-- Total Sales
-- Customer Rank

-- Concepts Used:
-- JOIN + CTE + Window Function


-- =============================================================
-- SECTION D : MINI PROJECT
-- =============================================================

-- MP1. Top 5 Customers

-- MP2. Bottom 5 Customers

-- MP3. Customers Who Made Only One Order

-- MP4. Customers Having Above Average Sales

-- MP5. Highest Order Value Per Customer


-- =============================================================
-- SECTION E : CONCLUSION
-- =============================================================

/*
This assignment demonstrates the use of SQL analytical
techniques such as Subqueries, CTEs, Window Functions,
and Joins on the Superstore dataset.

The analysis helped identify top-performing customers,
customer sales trends, and overall business performance.
These concepts are useful for data analysis and
business reporting in real-world scenarios.
*/