-- Task fifteen solution
-- this is the script solution for groups
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
