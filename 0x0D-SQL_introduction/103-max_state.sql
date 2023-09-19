--advanced task onoe o three solution
--this is the solution for max state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
