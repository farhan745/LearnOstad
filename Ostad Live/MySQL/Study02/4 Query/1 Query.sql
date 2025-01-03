/*
Simple Select Query Using Alias 
1. SQL aliases are used to give a table, or a column in a table, a temporary name.
2. Aliases are often used to make column names more readable.
3. An alias only exists for the duration of that query.
*/

SELECT a.firstName,a.lastName FROM users a 



/*
Inner Join With users And categories
1. Combines rows from two or more tables based on a related column between them
2. It returns only the rows that have matching values in both tables
3. If there is no match for the row in either left or right table, that row will not appear in the result set
*/

SELECT a.firstName, b.name FROM users a INNER JOIN categories b ON a.id=b.user_id WHERE a.id=1 
SELECT a.firstName, b.name FROM users a INNER JOIN categories b ON a.id=b.user_id WHERE b.id=5 
SELECT a.firstName, b.name FROM users a INNER JOIN categories b ON a.id=b.user_id WHERE b.name='Books'



/*
Left Join With users And categories
1. Combine rows from two or more tables based on a related column between them
2. It returns all the rows from the left table, with the matched rows from the right table
3. If there is no match, the result set will contain NULL values on the side of the right table
*/
SELECT a.firstName, b.name FROM users a LEFT JOIN categories b ON a.id=b.user_id WHERE a.id=1 
SELECT a.firstName, b.name FROM users a LEFT JOIN categories b ON a.id=b.user_id WHERE b.id=5 
SELECT a.firstName, b.name FROM users a LEFT JOIN categories b ON a.id=b.user_id WHERE b.name='Books'



/*
Right Join With users And categories
1. Returns all rows from the right table, and the matched rows from the left table
2. If there is no match found in the left table, NULL values will be returned for columns of the left table.
*/

SELECT b.firstName, a.name FROM categories a RIGHT JOIN users b ON a.user_id=b.id WHERE a.id=1 
SELECT b.firstName, a.name FROM categories a RIGHT JOIN users b ON a.user_id=b.id WHERE b.id=5 
SELECT b.firstName, a.name FROM categories a RIGHT JOIN users b ON a.user_id=b.id WHERE a.name='Books'




/*
FULL OUTER JOIN users And categories
1. Returns all rows when there is a match in either the left table, the right table, or both.
2. If there is no match for a particular row in either table, the result set will still include that row, but with NULL values in the columns from the table that does not have a match.
*/

SELECT a.firstName, b.name FROM users a LEFT JOIN categories b ON a.id=b.user_id UNION ALL
SELECT b.firstName, a.name FROM categories a RIGHT JOIN users b ON a.user_id=b.id



/*
CROSS JOIN JOIN users And categories
1. Returns all possible combinations of rows between two tables
2. That is, for every row in the first table, the CROSS JOIN will return every row in the second table
*/

SELECT a.firstName, b.name FROM users a CROSS JOIN categories b




/*
Select Invoice Where ID=1 With User & Customer
*/

SELECT a.total,a.discount,a.vat,a.payable,b.firstName,c.name FROM invoices a
LEFT JOIN users b  ON a.user_id=b.id 
LEFT JOIN customers c  ON a.customer_id=c.id


SELECT * FROM invoices a
LEFT JOIN users b  ON a.user_id=b.id 
LEFT JOIN customers c  ON a.customer_id=c.id


/*
Select Invoice Where ID=1 With User & Customer & Invoice Products & Products & category
*/

SELECT * FROM invoices a
LEFT JOIN users b  ON a.user_id=b.id 
LEFT JOIN customers c  ON a.customer_id=c.id
LEFT JOIN invoice_products d  ON a.id=d.invoice_id
LEFT JOIN products e  ON d.product_id=e.id
LEFT JOIN categories f  ON e.category_id=f.id