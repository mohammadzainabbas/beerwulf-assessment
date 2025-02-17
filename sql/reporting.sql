-- a. What are the bottom 3 nations in terms of revenue?
-- Aggregates revenue by nation, ordering ascending to quickly retrieve the lowest revenue nations.
SELECT n.N_NAME, SUM(f.REVENUE) AS TotalRevenue
FROM FACT_SALES f
JOIN DIM_CUSTOMER c ON f.CUSTOMER_KEY = c.C_CUSTKEY
JOIN NATION n ON c.C_NATIONKEY = n.N_NATIONKEY
GROUP BY n.N_NAME
ORDER BY TotalRevenue ASC
LIMIT 3;
-- Reason: Uses indexed join keys and aggregation to limit processing to 3 rows.

