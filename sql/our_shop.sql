CREATE DATABASE IF NOT EXISTS the_shop;
USE the_shop;

-- Table structure for "products"-table
CREATE TABLE IF NOT EXISTS products (
  id    INT unsigned NOT NULL AUTO_INCREMENT,
  pName  VARCHAR(150) NOT NULL,
  description   VARCHAR(500) NOT NULL,
  price INT(10) NOT NULL,
  picture VARCHAR(255) NOT NULL,
  PRIMARY KEY   (id)
);

-- Adding data to "products"-table
-- INSERT INTO products (pName, description, price, picture) VALUES
-- ();
