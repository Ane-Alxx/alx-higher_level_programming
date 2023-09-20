-- this is the task solution for 14
-- script/query for my genres
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres m ON tv_genres.id = m.genre_id
INNER JOIN tv_shows s ON m.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY tv_genres.name ASC;
