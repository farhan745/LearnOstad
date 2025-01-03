-- Active: 1728316517915@@127.0.0.1@3306@test2
--Table

CREATE TABLE employees(
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) ,
  city VARCHAR(50),
  salary DECIMAL(10,2)
) ;
DROP TABLE employee;