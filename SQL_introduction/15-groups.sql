-- Number by score
SELECT SCORE, COUNT(*) AS number From `second_table` GROUP BY score ORDER BY number DESC;