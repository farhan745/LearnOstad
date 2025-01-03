-- SELECT ALL  
SELECT * FROM `Employees`


-- SELECT Using Where
SELECT * FROM `Employees` WHERE `City`='Boston'

-- SELECT With Sort 
SELECT * FROM `Employees` ORDER BY id DESC

-- SELECT With Limit 
SELECT * FROM `Employees` LIMIT 4

-- SELECT With GROUP
SELECT `City` FROM `Employees` GROUP BY `City`

-- Select Unique 
SELECT DISTINCT City FROM `Employees`


-- MAX 
SELECT MAX(Salary) AS highest FROM `Employees`

SELECT * FROM `Employees` WHERE `Salary`=(SELECT MAX(Salary) FROM `Employees`)


-- MIN 
SELECT MIN(Salary) AS lowest FROM `Employees`

SELECT * FROM `Employees` WHERE `Salary`=(SELECT MIN(Salary) FROM `Employees`)


-- AVG
SELECT AVG(Salary) AS avarageSalary FROM `Employees`


-- SUM 
SELECT SUM(Salary) AS total FROM `Employees`

-- COUNT
SELECT COUNT(*) as total From `Employees`