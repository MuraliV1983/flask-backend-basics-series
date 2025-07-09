
-- Create Database
CREATE DATABASE IF NOT EXISTS rest_api CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

USE rest_api;

-- Create Table Users
DROP TABLE IF EXISTS users;
CREATE TABLE users
(
	user_id INTEGER NOT NULL AUTO_INCREMENT COMMENT'PK: PK_USER_ID',
    user_name VARCHAR(255) NOT NULL COMMENT'USER NAME',
    user_email VARCHAR(255) UNIQUE NOT NULL COMMENT'USER EMAIL',
    user_created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP() COMMENT'USER CREATED DATE',
    user_status TINYINT DEFAULT 1 NOT NULL COMMENT'0-InActive,1- Active,2- Deleted',
    CONSTRAINT PK_USER_ID PRIMARY KEY(user_id)
)ENGINE=InnoDB COMMENT='TABLE TO STORE THE USER DETAILS';

-- Sample User Data
INSERT INTO users(user_id,user_name,user_email) VALUES 
(1,'Murali','Murali@example.com'),(2,'E-Friend','E-Friend@example.com');
COMMIT;