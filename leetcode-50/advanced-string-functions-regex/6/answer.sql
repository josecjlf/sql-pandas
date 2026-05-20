# Write your MySQL query statement below
with temp as (
    select * from orders where order_date >= '2020-02-01' and order_date <= '2020-02-29'
)
select product_name, sum(unit) as unit from products p join temp t on p.product_id = t.product_id group by product_name having sum(unit) >= 100;