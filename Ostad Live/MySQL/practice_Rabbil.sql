-- Active: 1728316517915@@127.0.0.1@3306@rabbil

--COUNT
SELECT COUNT(*) FROM products;
--SUM
SELECT SUM(price) FROM products ;
--AVG/MAX/MIN
SELECT AVG(price) FROM products ;
SELECT MIN(price) FROM products ;
SELECT MAX(price) FROM products ;

/*PART - 3*/

SELECT * FROM products;
SELECT name,price,unit FROM products;
--Rename
SELECT a.name,(a.price),a.unit FROM products a ;
SELECT b.name FROM categories b ;

--JOIN QUERY
SELECT a.`firstName`,a.`lastName`,b.name FROM users a INNER JOIN categories b on a.id = b.id;
SELECT a.`firstName`,a.`lastName`,b.name FROM users a LEFT JOIN categories b on a.id = b.id;
SELECT a.`firstName`,a.`lastName`,b.name FROM users a RIGHT JOIN categories b on a.id = b.id;

/*PART - 4*/
--UPDATE?/DELETE/UPDATE

--DELETE
DELETE FROM users WHERE id = 2 ;

--UPDATE
UPDATE users SET  `firstName`="Farhan",`lastName`="ZAWAD",email="farhanzawad111@yahoo.com" where id = 1;

--INSERT
INSERT INTO users
(id,firstName,lastName,email,mobile,password,otp)
VALUES
(1,'A','B','C1','D','E','0'),
(2,'A','B','C1','D','E','231412')
