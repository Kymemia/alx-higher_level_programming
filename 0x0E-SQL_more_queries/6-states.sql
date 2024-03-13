-- creates DB, hbtn_0d_usa & the table, states inside the DB
CREATE DATABASE IF NOT EXISTS hbnt_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
