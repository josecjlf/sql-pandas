# Write your MySQL query statement below
select distinct(num) as ConsecutiveNums from
(select num, lag(num) over (order by id) as pos1, lag(num,2) over (order by id) as pos2 from logs) t
where pos1 = pos2 and pos1 = num;