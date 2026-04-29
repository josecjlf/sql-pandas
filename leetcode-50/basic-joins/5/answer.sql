# Write your MySQL query statement below
select machine_id, round(avg(total),3)  as processing_time
from(
select machine_id
, process_id
, max(timestamp) - min(timestamp) as total
from activity
group by machine_id, process_id) t
group by machine_id;