-- Advanced task one o one:
-- this is the script ssolution for avg temps
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
