--- Simple Select All 
SELECT * FROM products


--- Simple Column Select
SELECT name,price,unit FROM products

--- Simple Select Query Using Alias --a(products) b(categories)
SELECT a.name FROM products a
SELECT b.name FROM categories b

--- JOIN Query users->a categories->b
---> গাইবান্ধা আত্মীয় রংপুর অন ছেলে=মেয়ে 
SELECT a.firstName, a.lastName , b.name, b.created_at FROM users a  INNER JOIN  categories b  ON a.id=b.user_id

SELECT a.firstName, a.lastName , b.name, b.created_at FROM users a  LEFT JOIN  categories b  ON a.id=b.user_id

SELECT a.firstName, a.lastName , b.name, b.created_at FROM users a  RIGHT JOIN  categories b  ON a.id=b.user_id


SELECT a.firstName, a.lastName , b.name, b.created_at FROM users a  CROSS JOIN  categories b  ON a.id=b.user_id



