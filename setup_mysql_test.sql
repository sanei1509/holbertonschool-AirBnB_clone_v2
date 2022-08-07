-- script que cree:
-- * database y usuario con todos los permisos
-- * contraseña y nombres especificados
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev'@'localhost';
-- GRANT SELECT ON performance_schema * TO 'hbnb_dev'@'localhost';
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';