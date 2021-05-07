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
('Stone', 'Common stone.', 9000, '/var/App/static/images/curtis-hystad-twClBGWNo-g-unsplash.jpg'),
('Bulb', 'This will light your way', 400, '/App/static/images/robert-wiedemann-d9yOg5zP-oQ-unsplash.jpg'),
('Shoe', 'Sigle left shoe of the brand Converse.', 60000, '/App/static/images/breezy-hanson-AXOF4dPcg2g-unsplash.jpg'),
('Peas', 'Peas in a pod. Yum yum!', 2500, '/App/static/images/rachael-gorjestani-XlA2994Txhw-unsplash.jpg'),
('Glass of Water', 'A glass of water. Is it alomst full or barely empty?', 333, '/App/static/images/mateusz-butkiewicz-jNk0_Bpd_xw-unsplash.jpg'),
('Twig', 'Common twig. Has many uses. You can reach stuff that was out of reach before', 999, '/App/static/images/przemyslaw-zientala-54bRSFZkSGg-unsplash.jpg'),
('Bucket', 'An ordinary bucket. Use it as a hat, use it to carry water, or use it to stand on.', 5555, '/App/static/images/lucas-van-oort-LVJRzXqbJ1s-unsplash.jpg');

# A user with read-only access to a single table
-- CREATE USER 'anonymous' IDENTIFIED BY 'root';
-- GRANT SELECT ON the_shop TO 'anonymous';
