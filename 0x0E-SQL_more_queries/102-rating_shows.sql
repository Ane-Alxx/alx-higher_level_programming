-- this is the solution for task 102
-- script/query for rating shows
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rat
FROM tv_shows
INNER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_show_ratings.show_id
ORDER BY rat DESC;
