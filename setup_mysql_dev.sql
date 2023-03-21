-- prepare a MySQL dev server for the AirBnB_console_v2 project

CREATE DATABASE IF NOT EXISTS hbtn_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* 'hbnb_dev'@'localhost';
