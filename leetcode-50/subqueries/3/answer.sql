(select u.name as results from users u
join movierating m
on u.user_id = m.user_id
group by u.name
order by count(*) DESC, u.name ASC
limit 1)
union all
(select mv.title from movierating mr
join movies mv
on mr.movie_id = mv.movie_id
where created_at between '2020-02-01' and '2020-02-29'
group by mr.movie_id, mv.title
order by avg(rating) DESC, mv.title ASC
limit 1);