# Write your MySQL query statement below
select employee_id from employees e
where e.manager_id is not null and e.salary < 30000 and not exists (select 1 from employees m WHERE e.manager_id = m.employee_id)
order by employee_id;