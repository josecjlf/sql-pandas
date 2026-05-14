# Write your MySQL query statement below
with temp as (
select d.name as Department
, e.name as Employee
,salary as Salary
, dense_rank() over (partition by departmentId order by salary desc) as total
from employee e join department d on e.departmentId = d.id)
select Department, Employee, Salary from temp where total in(1,2,3);