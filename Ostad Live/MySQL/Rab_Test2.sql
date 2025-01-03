CREATE TABLE users(
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  firstName VARCHAR(50)NOT NULL,
  lastName VARCHAR(50)NOT NULL,
  Email VARCHAR(50)NOT NULL,
  mobileNumber VARCHAR(50)NOT NULL,
  password VARCHAR(500) NOT NULL,
  otp VARCHAR(10) NOT NULL DEFAULT '0',
  create_at TIMESTAMP NOT NULL DEFAULT current_timestamp(),
  updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)

CREATE TABLE catgories(
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  user_id BIGINT UNSIGNED NOT NULL ,
  FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  create_at TIMESTAMP NOT NULL DEFAULT current_timestamp(),
  updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
  )

CREATE TABLE products(
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  price VARCHAR(50) NOT NULL,
  unit VARCHAR(50) NOT NULL,
  user_id BIGINT UNSIGNED NOT NULL,
  category_id BIGINT UNSIGNED NOT NULL,
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`category_id`) REFERENCES catgories(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  create_at TIMESTAMP NOT NULL DEFAULT current_timestamp(),
  updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)

CREATE TABLE customers(
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50)NOT NULL,
  phoneNumber VARCHAR(50)NOT NULL,
  user_id BIGINT UNSIGNED NOT NULL,
  Foreign Key (`user_id`) REFERENCES users(`id`) ON Delete RESTRICT ON UPDATE CASCADE,
  create_at TIMESTAMP NOT NULL DEFAULT current_timestamp(),
  updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
  )

CREATE TABLE invoices(
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  total VARCHAR(50) NOT NULL,
  discount VARCHAR(50)NOT NULL,
  vat VARCHAR(50)NOT NULL,
  payable VARCHAR(50)NOT NULL,
  user_id BIGINT UNSIGNED NOT NULL,
  customer_id BIGINT UNSIGNED NOT NULL,
  Foreign Key (`user_id`) REFERENCES users(`id`) ON Delete RESTRICT ON UPDATE CASCADE,
  Foreign Key (`customer_id`) REFERENCES customers(`id`) ON Delete RESTRICT ON UPDATE CASCADE,
  create_at TIMESTAMP NOT NULL DEFAULT current_timestamp(),
  updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)

CREATE TABLE invoice_products(
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  qty VARCHAR(50) NOT NULL,
  sale_price VARCHAR(50) NOT NULL,
  user_id BIGINT UNSIGNED NOT NULL,
  product_id BIGINT UNSIGNED NOT NULL,
  invoice_id BIGINT UNSIGNED NOT NULL,
  Foreign Key (`user_id`) REFERENCES users(`id`) ON Delete RESTRICT ON UPDATE CASCADE,
  Foreign Key (`product_id`) REFERENCES products(`id`) ON Delete RESTRICT ON UPDATE CASCADE,
  Foreign Key (`invoice_id`) REFERENCES invoices(`id`) ON Delete RESTRICT ON UPDATE CASCADE,
  create_at TIMESTAMP NOT NULL DEFAULT current_timestamp(),
  updated_at TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
)


DROP TABLE catgories;