--advanced task one o two solution
--this is the solution for top city
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
