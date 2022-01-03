-- lists the number of records with the same score in the table second_table

SELECT COUNT(id) AS number, score FROM second_table GROUP BY score ORDER BY number DESC;
