import sqlalchemy as sa
import os
import pandas as pd


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
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
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# setup of a user and a database that would contain time series

engine2 = sa.create_engine("mysql+mysqldb://root:pass@localhost/")
connection2 = engine2.connect()
command1 = "CREATE DATABASE IF NOT EXISTS time_series;"
connection2.execute(command1)
command2 = "CREATE USER IF NOT EXISTS 'ts_user'@'localhost' identified by 'test1234';"
connection2.execute(command2)
command3 = "GRANT ALL ON time_series.* TO 'ts_user'@'localhost';"
connection2.execute(command3)
connection2.close()

# get some data
data_folder = os.path.join(os.getcwd(), "data")
df_oil = pd.read_csv(os.path.join(data_folder, "cl_f_d.csv"))
df_gas = pd.read_csv(os.path.join(data_folder, "ng_f_d.csv"))
df_wig20 = pd.read_csv(os.path.join(data_folder, "wig20_d.csv"))

# rename & keep columns of interest only
names_dict = {"Data": "date", "Otwarcie": "open", "Zamkniecie": "close"}
df_oil.rename(columns=names_dict, inplace=True)
df_oil = df_oil[list(names_dict.values())]
df_gas.rename(columns=names_dict, inplace=True)
df_gas = df_gas[list(names_dict.values())]
df_wig20.rename(columns=names_dict, inplace=True)
df_wig20 = df_wig20[list(names_dict.values())]

# transforming data frames into long-format
dict_of_dfs = {"oil": df_oil, "gas": df_gas, "wig20": df_wig20}
for iter_key, iter_val in dict_of_dfs.items():
    dict_of_dfs[iter_key] = iter_val.melt(id_vars="date", value_vars=["open", "close"], var_name="variable_name")

df_full_long = pd.concat(tuple(dict_of_dfs.values()), keys=list(dict_of_dfs.keys()))
df_full_long.reset_index(inplace=True, drop=False)
df_full_long.drop("level_1", axis=1, inplace=True)
df_full_long.rename(columns={"level_0": "asset_name"}, inplace=True)
print(df_full_long.head())
print(df_full_long.tail())
df_full_long.loc[:, "date"] = [pd.Timestamp(el) for el in df_full_long.loc[:, "date"]]
print(df_full_long.dtypes)

# uploading the data into the database
engine3 = sa.create_engine("mysql+mysqldb://ts_user:test1234@localhost/time_series")
connection3 = engine3.connect()

# upload the data into a MySQL table
df_full_long.to_sql(name="my_table", con=connection3, if_exists="append",
                    dtype={"asset_name": sa.VARCHAR(20), "date": sa.DATE,
                           "variable_name": sa.VARCHAR(20), "value": sa.FLOAT}, index=True)
connection3.close()
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# note, that th index of the table my_table is not very neat; to better control the table structure, better create
# the table manually in the first place

# create a custom table first
engine4 = sa.create_engine("mysql+mysqldb://ts_user:test1234@localhost/time_series")
metadata4 = sa.MetaData(engine4)
sa.Table("my_custom_table", metadata4,
         sa.Column("data_index", sa.BIGINT, nullable=False, autoincrement=True, primary_key=True),
         sa.Column("asset_name", sa.VARCHAR(20), nullable=False),
         sa.Column("date", sa.DATE, nullable=False),
         sa.Column("variable_name", sa.VARCHAR(20), nullable=False),
         sa.Column("value", sa.FLOAT(10, 2), nullable=False)
         )
metadata4.create_all()


# load the data afterwards
df_full_long.reset_index(inplace=True, drop=False)
df_full_long.rename(columns={"index": "data_index"}, inplace=True)
df_full_long.head()
df_full_long.loc[:, "data_index"] = df_full_long.loc[:, "data_index"] + 1

connection4 = engine4.connect()
df_full_long.to_sql(con=connection4, name="my_custom_table", if_exists="append", index=False)
connection4.close()

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# INSERT in SQL and in SQLAlchemy
engine5 = sa.create_engine("mysql+mysqldb://ts_user:test1234@localhost/time_series")
metadata5 = sa.MetaData(bind=engine5)
my_tab_1 = sa.Table("my_tab_1", metadata5,
         sa.Column("index_col", sa.INT, nullable=False, primary_key=True),
         sa.Column("char_col", sa.VARCHAR(50), nullable=False),
         sa.Column("int_col", sa.INT, nullable=False)
         )
metadata5.create_all()

connection5 = engine5.connect()
# create an insert command
insert_temp = my_tab_1.insert().values(index_col=1, char_col="asdf", int_col=3213)
# execute the insert command
connection5.execute(insert_temp)
connection5.close()

# now, insert a row manually - using raw SQL command
connection5 = engine5.connect()
insert_command = "INSERT INTO time_series.my_tab_1 (index_col, char_col, int_col) VALUES (2, 'qqq', 323);"
connection5.execute(insert_command)
connection5.close()

del connection5, engine5
# ----------------------------------------------------------------------------------------------------------------------

