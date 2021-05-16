CREATE DATABASE IF NOT EXISTS the_shop;
USE the_shop;
drop table products;
-- Table structure for "products"-table
CREATE TABLE IF NOT EXISTS products (
  id    INT unsigned NOT NULL AUTO_INCREMENT,
  pName  VARCHAR(150) NOT NULL,
  description   VARCHAR(500) NOT NULL,
  price INT(10) NOT NULL,
  picture VARCHAR(300) NOT NULL,
  PRIMARY KEY   (id)
);

DESCRIBE products;

-- Adding data to "products"-table
INSERT INTO products (pName, description, price, picture) VALUES
('Stone', 'Common stone.', 9000, 'https://images.unsplash.com/photo-1481015771284-59ea3dee95af?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1276&q=80'),
('Bulb', 'This will light your way', 400, 'https://images.unsplash.com/photo-1485119502162-016e4409beab?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2100&q=80'),
('Shoe', 'Sigle left shoe of the brand Converse.', 60000, 'https://images.unsplash.com/photo-1616736381029-c403eeda10b8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2378&q=80'),
('Peas', 'Peas in a pod. Yum yum!', 2500, 'https://images.unsplash.com/photo-1477506252414-b2954dbdacf3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2100&q=80'),
('Glass of Water', 'A glass of water. Is it alomst full or barely empty?', 333, 'https://images.unsplash.com/photo-1612375066516-11d6d394bd2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1300&q=80'),
('Twig', 'Common twig. Has many uses. You can reach stuff that was out of reach before', 999, 'https://images.unsplash.com/photo-1521126598398-60d23e6f4eee?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1867&q=80'),
('Bucket', 'An ordinary bucket. Use it as a hat, use it to carry water, or use it to stand on.', 5555, 'https://images.unsplash.com/photo-1589630388147-68b3a2172e0c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2100&q=80');

# A user with read-only access to a single table
-- CREATE USER 'anonymous' IDENTIFIED BY 'root';
-- GRANT SELECT ON the_shop TO 'anonymous';
