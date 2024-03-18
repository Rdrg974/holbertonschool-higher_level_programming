-- Number by score
SELECT `score`, COUNT(*) AS `number` From `second_table` GROUP BY `score` ORDER BY `number` DESC;