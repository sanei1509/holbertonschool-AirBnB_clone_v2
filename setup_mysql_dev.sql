-- script que cree:
-- * database y usuario con todos los permisos
-- * contraseña y nombres especificados
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev'@'localhost';
-- GRANT SELECT ON performance_schema * TO 'hbnb_dev'@'localhost';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';