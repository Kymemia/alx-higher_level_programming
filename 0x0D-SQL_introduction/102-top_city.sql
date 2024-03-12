-- displays the top 3 cities temperatures during July & August (DESC. order)
LOAD DATA INFILE '/home/kimkim/Downloads/temperatures(1).sql'
INTO TABLE hbtn_0c_0
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

SELECT city, AVG(value) as avg_temp FROM temperatures
WHERE month = 7 OR month = 8 GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
