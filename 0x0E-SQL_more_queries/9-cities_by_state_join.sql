-- this is the solution
-- this is the script/query cities by state join
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
