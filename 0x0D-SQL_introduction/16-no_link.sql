-- lists all records of the table second_table of the database except those
-- without name 
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != "" 
ORDER BY `score` DESC;
