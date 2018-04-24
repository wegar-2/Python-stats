### BASIC COMMANDS THAT ALLOW YOUTO WORK WITH MYSQL ARE COLLECTED HERE ###

### 1. Logging as user the_user from command line and passing a password
### 	mysql -u the_user -p

### 2. Viewing databses
SHOW databases;

### 3. Selecting a specific database
USE information_schema;

### 4. Viewing all the table that exist on the information_schema
SHOW TABLES;

### 5. Creating a user the_user at host hostname
CREATE USER 'the_user'@'localhost' identified by 'user_account_password';

### 6. Deleting a user
DROP USER IF EXISTS 'the_user'@'localhost';

### 7. Granting privileges to a user:
GRANT ALL PRIVILEGES ON DATABASE_NAME.* TO 'the_user'@'localhost';

### 8. What are the different privileges that can be endowed?
### 8.1. CREATE
### 8.2. DELETE
### 8.3. INSERT
### 8.4. SELECT
### 8.5. UPDATE

### 9. REVOKING the prvileges that have been granted

REVOKE SELECT, INSERT ON DATABASE_NAME.TABLE_NAME FROM 'the_user'@'localhost';


### 10. Creating database my_database

CREATE DATABASE my_database;


### 11. 
