-- this is the solution for task 103
-- script/query for rating genres
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rat
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_show_genres.genre_id
ORDER BY rat DESC;
