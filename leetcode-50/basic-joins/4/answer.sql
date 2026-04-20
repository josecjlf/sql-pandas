# Write your MySQL query statement below
select Id from (select id, 
recorddate,
temperature, 
lag(temperature) over (order by recorddate) as prev_temp,
lag(recorddate) over (order by recorddate) as prev_date
from weather) t
where temperature > prev_temp and recorddate = date_add(prev_date, interval 1 day);