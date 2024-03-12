-- displays the average temperature(F) by city in descending format
LOAD DATA INFILE '/home/kimkim/Downloads/temperatures.sql'
INTO TABLE hbtn_0c_0
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

SELECT city, AVG(value) as avg_temp
FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
