-- this is the solution for task 5
-- script/query for unique id
CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
