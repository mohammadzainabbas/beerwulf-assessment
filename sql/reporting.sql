----------------------------------------------------------------------------------------------------------------------------
-- a. What are the bottom 3 nations in terms of revenue?
----------------------------------------------------------------------------------------------------------------------------
-- Aggregates revenue by nation, ordering ascending to quickly retrieve the lowest revenue nations.
----------------------------------------------------------------------------------------------------------------------------
SELECT 'a. What are the bottom 3 nations in terms of revenue?' AS Question;
SELECT '';  -- Blank line for readability
SELECT n.N_NAME AS Nation, SUM(f.REVENUE) AS TotalRevenue
FROM FACT_SALES f
JOIN DIM_CUSTOMER c ON f.CUSTOMER_KEY = c.C_CUSTKEY
JOIN NATION n ON c.C_NATIONKEY = n.N_NATIONKEY
GROUP BY n.N_NAME
ORDER BY TotalRevenue ASC
LIMIT 3;
SELECT '';  -- Blank line for readability
----------------------------------------------------------------------------------------------------------------------------
-- Reason: Uses indexed join keys and aggregation to limit processing to 3 rows.
----------------------------------------------------------------------------------------------------------------------------


----------------------------------------------------------------------------------------------------------------------------
-- b. From the top 3 nations, what is the most common shipping mode ?
----------------------------------------------------------------------------------------------------------------------------
-- Uses a CTE to first identify top nations and then determines the most frequent shipping mode.
----------------------------------------------------------------------------------------------------------------------------
SELECT 'b. From the top 3 nations, what is the most common shipping mode?' AS Question;
SELECT '';  -- Blank line for readability
WITH TopNations AS (
  SELECT n.N_NATIONKEY, n.N_NAME, SUM(f.REVENUE) AS TotalRevenue
  FROM FACT_SALES f
  JOIN DIM_CUSTOMER c ON f.CUSTOMER_KEY = c.C_CUSTKEY
  JOIN NATION n ON c.C_NATIONKEY = n.N_NATIONKEY
  GROUP BY n.N_NATIONKEY, n.N_NAME
  ORDER BY TotalRevenue DESC
  LIMIT 3
)
SELECT f.SHIP_MODE AS CommonShipMode, COUNT(*) AS ModeCount
FROM FACT_SALES f
JOIN DIM_CUSTOMER c ON f.CUSTOMER_KEY = c.C_CUSTKEY
JOIN TopNations t ON c.C_NATIONKEY = t.N_NATIONKEY
GROUP BY f.SHIP_MODE
ORDER BY ModeCount DESC
LIMIT 1;
SELECT '';  -- Blank line for readability
----------------------------------------------------------------------------------------------------------------------------
-- Reason: The CTE isolates the top nations, and the join is optimized via indexed foreign keys.
----------------------------------------------------------------------------------------------------------------------------


----------------------------------------------------------------------------------------------------------------------------
-- c. What are the top 5 selling months?
----------------------------------------------------------------------------------------------------------------------------
-- Aggregates revenue by month using strftime to format dates; grouping and ordering quickly surfaces top months.
----------------------------------------------------------------------------------------------------------------------------
SELECT 'c. What are the top 5 selling months?' AS Question;
SELECT '';  -- Blank line for readability
SELECT strftime('%Y-%m', ORDER_DATE) AS Month, SUM(REVENUE) AS TotalRevenue
FROM FACT_SALES
GROUP BY Month
ORDER BY TotalRevenue DESC
LIMIT 5;
SELECT '';  -- Blank line for readability
----------------------------------------------------------------------------------------------------------------------------
-- Reason: Computation on ORDER_DATE is minimized by grouping on the formatted month, ensuring efficient aggregation.
----------------------------------------------------------------------------------------------------------------------------


----------------------------------------------------------------------------------------------------------------------------
-- d. Who are the top customer(s) in terms of either revenue or quantity?
----------------------------------------------------------------------------------------------------------------------------
-- Aggregates both revenue and quantity per customer, ordering by revenue and quantity to identify top customers.
----------------------------------------------------------------------------------------------------------------------------
SELECT 'd. Who are the top customer(s) in terms of either revenue or quantity?' AS Question;
SELECT '';  -- Blank line for readability
SELECT c.C_NAME AS CustomerName, SUM(f.REVENUE) AS TotalRevenue, SUM(f.QUANTITY) AS TotalQuantity
FROM FACT_SALES f
JOIN DIM_CUSTOMER c ON f.CUSTOMER_KEY = c.C_CUSTKEY
GROUP BY c.C_CUSTKEY
ORDER BY TotalRevenue DESC, TotalQuantity DESC
LIMIT 1;
SELECT '';  -- Blank line for readability
----------------------------------------------------------------------------------------------------------------------------
-- Reason: Composite ordering using indexed customer keys allows for a rapid lookup of top-performing customers.
----------------------------------------------------------------------------------------------------------------------------


----------------------------------------------------------------------------------------------------------------------------
-- e. Year-to-year (01 July to 30 June) revenue comparison
----------------------------------------------------------------------------------------------------------------------------
-- Uses CASE to group orders into financial years and aggregates revenue, ideal for financial reporting.
----------------------------------------------------------------------------------------------------------------------------
SELECT 'e. Year-to-year (01 July to 30 June) revenue comparison' AS Question;
SELECT '';  -- Blank line for readability
SELECT 
  CASE 
    WHEN strftime('%m', ORDER_DATE) >= '07' THEN strftime('%Y', ORDER_DATE)
    ELSE strftime('%Y', ORDER_DATE) - 1
  END AS FinancialYear,
  SUM(REVENUE) AS TotalRevenue
FROM FACT_SALES
GROUP BY FinancialYear
ORDER BY FinancialYear;
SELECT '';  -- Blank line for readability
----------------------------------------------------------------------------------------------------------------------------
-- Reason: Computed grouping on financial year reduces processing overhead by collapsing data into fewer groups.
----------------------------------------------------------------------------------------------------------------------------