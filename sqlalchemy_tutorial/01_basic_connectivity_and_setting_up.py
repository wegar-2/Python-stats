import sqlalchemy as sa

# first thing that is needed to connect to a database is a connection engine
engine1 = sa.create_engine("mysql://test_user:test1234@localhost/test_db")

# secondly, establish a connection
connection1 = engine1.connect()

# thirdly, execute a sample command
test_command = " CREATE TABLE IF NOT EXISTS test_db.table_1 (" \
               "varchar_column VARCHAR(20) NULL," \
               "int_column INT NULL," \
               "date_column DATE NULL" \
               "); "
connection1.execute(test_command)

# finally, close the connection
connection1.close()

