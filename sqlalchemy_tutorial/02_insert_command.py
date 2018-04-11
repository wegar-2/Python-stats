import sqlalchemy as sa
import numpy as np
import string

# prepare connection
engine1 = sa.create_engine("mysql://test_user:test1234@localhost/test_db")
connection1 = engine1.connect()

# raw SQL insert statement
insert_raw_cmd = "INSERT INTO table_1 (varchar_column, int_column) VALUES ('asdf', 123);"
connection1.execute(insert_raw_cmd)


# do some more insert statements using random texts and numbers
def make_a_word(list_of_nums):
    return "".join([string.ascii_uppercase[j] for j in list_of_nums])


for el in range(10000):
    iter_word = make_a_word(list(np.random.randint(low=0, high=len(string.ascii_uppercase), size=5)))
    iter_num = np.random.randint(low=1, high=101, size=1)
    iter_cmd = "INSERT INTO test_db.table_1(varchar_column, int_column) VALUES ('" + \
               iter_word + "' , " + str(iter_num[0]) + ");"
    connection1.execute(iter_cmd)


