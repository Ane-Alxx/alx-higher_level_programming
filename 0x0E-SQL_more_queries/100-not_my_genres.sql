-- this is the solution for task 100
-- this is a script/query for not my genres

SELECT DISTINCT `name`
  FROM `tv_genres` AS gen
       INNER JOIN `tv_show_genres` AS sw
       ON gen.`id` = sw.`genre_id`

       INNER JOIN `tv_shows` AS ts
       ON sw.`show_id` = ts.`id`
       WHERE gen.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS gen
	             INNER JOIN `tv_show_genres` AS sw
		     ON gen.`id` = sw.`genre_id`

		     INNER JOIN `tv_shows` AS ts
		     ON sw.`show_id` = ts.`id`
		     WHERE ts.`title` = "Dexter")
 ORDER BY gen.`name`;
