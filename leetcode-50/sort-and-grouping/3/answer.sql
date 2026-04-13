# Write your MySQL query statement below

WITH temp AS (
    SELECT 
        product_id, 
        year,
        quantity,
        price,
        RANK() OVER (
            PARTITION BY product_id
            ORDER BY year asc
        ) AS t
    FROM Sales
)
SELECT product_id, year as first_year, quantity, price
FROM temp
WHERE t = 1;
