# Write your MySQL query statement below
SELECT (
    SELECT distinct salary
    FROM employee
    ORDER BY salary desc
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;