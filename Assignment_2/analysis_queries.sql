CREATE DATABASE superstore_db;
USE superstore_db;

SELECT COUNT(*) AS Total_Rows
FROM `sample - superstore`;

SELECT *
FROM `sample - superstore`
LIMIT 10;

SHOW COLUMNS
FROM `sample - superstore`;

SELECT DISTINCT Category
FROM `sample - superstore`;

SELECT DISTINCT Region
FROM `sample - superstore`;

SELECT *
FROM `sample - superstore`
WHERE Region='West';

SELECT *
FROM `sample - superstore`
WHERE Category='Technology';

SELECT *
FROM `sample - superstore`
WHERE Sales > 500;

SELECT *
FROM `sample - superstore`
WHERE Region='East'
AND Category='Furniture'
AND Sales > 300;

SELECT Region,
SUM(Sales) AS Total_Sales
FROM `sample - superstore`
GROUP BY Region;

SELECT Category,
SUM(Sales) AS Total_Sales
FROM `sample - superstore`
GROUP BY Category;

SELECT Category,
SUM(Quantity) AS Total_Quantity
FROM `sample - superstore`
GROUP BY Category;

SELECT Category,
AVG(Profit) AS Average_Profit
FROM `sample - superstore`
GROUP BY Category;

SELECT `Product Name`,
SUM(Sales) AS Total_Sales
FROM `sample - superstore`
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT Category,
SUM(Sales) AS Total_Sales
FROM `sample - superstore`
GROUP BY Category
ORDER BY Total_Sales DESC;

SELECT `Customer Name`,
SUM(Sales) AS Total_Sales
FROM `sample - superstore`
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT `Product Name`,
SUM(Quantity) AS Total_Quantity
FROM `sample - superstore`
GROUP BY `Product Name`
ORDER BY Total_Quantity DESC
LIMIT 10;

SELECT
YEAR(STR_TO_DATE(`Order Date`,'%d-%m-%Y')) AS Year,
MONTH(STR_TO_DATE(`Order Date`,'%d-%m-%Y')) AS Month,
SUM(Sales) AS Total_Sales
FROM `sample - superstore`
GROUP BY Year, Month
ORDER BY Year, Month;

SELECT `Customer Name`,
SUM(Sales) AS Total_Sales
FROM `sample - superstore`
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT `Order ID`,
COUNT(*) AS Duplicate_Count
FROM `sample - superstore`
GROUP BY `Order ID`
HAVING COUNT(*) > 1;

SELECT
SUM(CASE WHEN Sales IS NULL THEN 1 ELSE 0 END) AS Missing_Sales,
SUM(CASE WHEN Quantity IS NULL THEN 1 ELSE 0 END) AS Missing_Quantity,
SUM(CASE WHEN Profit IS NULL THEN 1 ELSE 0 END) AS Missing_Profit
FROM `sample - superstore`;

SELECT `Order ID`,
COUNT(*)
FROM `sample - superstore`
GROUP BY `Order ID`
HAVING COUNT(*) > 1;

SELECT *
FROM `sample - superstore`
WHERE Sales < 0;

SELECT DISTINCT Category
FROM `sample - superstore`;