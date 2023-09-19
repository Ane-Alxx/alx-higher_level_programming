--Task sixteen solution
--this is the script query for no linlk
SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;
