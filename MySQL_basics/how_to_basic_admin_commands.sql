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

