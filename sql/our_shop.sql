CREATE DATABASE IF NOT EXISTS the_shop;
USE the_shop;
drop table products;
-- Table structure for "products"-table
CREATE TABLE IF NOT EXISTS products (
  id    INT unsigned NOT NULL AUTO_INCREMENT,
  pName  VARCHAR(150) NOT NULL,
  description   VARCHAR(500) NOT NULL,
  price INT(10) NOT NULL,
  picture VARCHAR(255) NOT NULL,
  PRIMARY KEY   (id)
);

DESCRIBE products;

-- Adding data to "products"-table
INSERT INTO products (pName, description, price, picture) VALUES
-- ('Stone', 'Common stone.', 9000, LOAD_FILE('DATA2410_Portfolio2_Task1/App/images/curtis-hystad-twClBGWNo-g-unsplash.jpg')),
('Bulb', 'This will light your way', 400, '...'),
('Shoe', 'Sigle left shoe of the brand Converse.', 60000, '...');

# A user with read-only access to a single table
-- CREATE USER 'anonymous' IDENTIFIED BY 'PiWaC!23CyZzkAYYpi&2S';
-- GRANT SELECT ON the_shop TO 'anonymous';
