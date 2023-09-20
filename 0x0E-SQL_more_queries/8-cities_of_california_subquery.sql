-- this is the solution for task 8
-- this is the script/query for create cities
-- of california subquery
SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;
