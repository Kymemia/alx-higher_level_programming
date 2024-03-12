-- lists number of records with the same score in second_table of DB, hbtn_0c_0
SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
