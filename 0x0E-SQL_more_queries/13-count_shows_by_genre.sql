-- this is the solution for task 13
-- this is a script/query for show by genre
SELECT tv_genres.name AS genre, COUNT(*) AS show_counts
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY show_counts DESC;
