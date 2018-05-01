import sqlalchemy as sa
import numpy as np
import string

# prepare connection
engine1 = sa.create_engine("mysql://test_user:test1234@localhost/test_db")
connection1 = engine1.connect()


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 1. using raw SQL insert command

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

connection1.close()
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 2. using SQLAlchemy's insert() command
engine2 = sa.create_engine("mysql+mysqldb://test_user:test1234@localhost/test_db")
connection2 = engine2.connect()
metadata2 = sa.MetaData(bind=engine2)

my_table = sa.Table("my_table", metadata2,
                    sa.Column("index_column", sa.INT, nullable=False, autoincrement=True),
                    sa.Column("text_column", sa.VARCHAR(20), nullable=False)
                    )
metadata2.create_all()

ins_cmd = my_table.insert().values(index_column=1, text_column="qwerty")
connection2.execute(ins_cmd)
connection2.close()
# ----------------------------------------------------------------------------------------------------------------------

