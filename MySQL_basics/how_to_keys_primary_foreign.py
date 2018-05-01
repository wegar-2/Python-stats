import sqlalchemy as sa
import pandas as pd

# in this script, use of keys: primary and foreign is presented

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 1. create temporary DB and user
setup_engine = sa.create_engine("mysql+mysqldb://root:pass@localhost/")
setup_connection = setup_engine.connect()
cmd_database = "CREATE DATABASE IF NOT EXISTS temp_db;"
setup_connection.execute(cmd_database)
cmd_user = "CREATE USER IF NOT EXISTS 'temp_user'@'localhost' IDENTIFIED BY 'temp_pass';"
setup_connection.execute(cmd_user)
cmd_privs = "GRANT ALL ON temp_db.* TO 'temp_user'@'localhost';"
setup_connection.execute(cmd_privs)
setup_connection.close()
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 2. create two tables with keys and foreign key - using raw SQL commands
engine2 = sa.create_engine("mysql+mysqldb://temp_user:temp_pass@localhost/temp_db")
connection2 = engine2.connect()
# 2.1. create two tables
cmd_table1 = "CREATE TABLE clients (" \
             "  client_id INT(10) NOT NULL auto_increment," \
             "  client_name VARCHAR(20) NOT NULL," \
             "  client_surname VARCHAR(20) NOT NULL," \
             "  client_value FLOAT(12, 2) NOT NULL," \
             "  PRIMARY KEY(client_id)" \
             ");"
connection2.execute(cmd_table1)

cmd_table2 = "CREATE TABLE orders (" \
             "  order_id INT(10) NOT NULL auto_increment," \
             "  order_name VARCHAR(20) NOT NULL," \
             "  order_client_id INT(10) NOT NULL," \
             "  PRIMARY KEY(order_id)," \
             "  FOREIGN KEY(order_client_id) REFERENCES clients(client_id)" \
             ");"
connection2.execute(cmd_table2)


# 2.2. populate the tables and do some simple queries
insert1 = "INSERT INTO clients(client_name, client_surname, client_value) " \
          "VALUES('John', 'McRonald', 123.3);"
insert2 = "INSERT INTO clients(client_name, client_surname, client_value) " \
          "VALUES('Jessica', 'Grant', 910.22);"
insert3 = "INSERT INTO clients(client_name, client_surname, client_value) " \
          "VALUES('Butch', 'McKenzie', 123.3);"
connection2.execute(insert1)
connection2.execute(insert2)
connection2.execute(insert3)

insert4 = "INSERT INTO orders(order_name, order_client_id) " \
          "VALUES ('big car', 1);"
insert5 = "INSERT INTO orders(order_name, order_client_id) " \
          "VALUES ('painting', 3);"
insert6 = "INSERT INTO orders(order_name, order_client_id) " \
          "VALUES ('gun', 2);"
insert7 = "INSERT INTO orders(order_name, order_client_id) " \
          "VALUES ('book', 2);"
connection2.execute(insert4)
connection2.execute(insert5)
connection2.execute(insert6)
connection2.execute(insert7)

sample_query = "SELECT a.* " \
               "FROM (" \
               "    SELECT lt.*, rt.*" \
               "    FROM clients lt" \
               "    LEFT JOIN orders rt" \
               "    ON lt.client_id = rt.order_client_id" \
               ") a " \
               " WHERE a.client_id = 2;"
query_result = connection2.execute(sample_query)

for iter_val in query_result.fetchall():
    print(iter_val)

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 3. repeat exercise from the above using SQLAlchemy syntax

# ----------------------------------------------------------------------------------------------------------------------

