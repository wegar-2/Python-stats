import pandas as pd
import logging
import os
import sqlalchemy as sa

# setup a logger
logger1 = logging.getLogger(name="logger1")
logger1.setLevel(level=logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(level=logging.INFO)

fmt = logging.Formatter(fmt=" - - - ")


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# data preparation
sample_path = os.path.join("~", "github_repos", "Python-stats", "sqlalchemy_tutorial", "04_revision_script.py")
# this_script_path = os.path.dirname(path=__file__)
data_folder_path = os.path.join(os.path.dirname(os.path.dirname(sample_path)), "data2")

files = os.listdir(os.path.expanduser(data_folder_path))

# load the data from, CSV files into DataFrames
dict_of_dfs = {}
for file in files:
    # load the data from a file
    file_path = os.path.join(os.path.expanduser(data_folder_path), file)
    df_temp = pd.read_csv(file_path)
    # transform the data
    dict_new_names = {"Data": "date", "Otwarcie": "open", "Zamkniecie": "close",
                      "Najwyzszy": "high", "Najnizszy": "low"}
    df_temp.rename(columns=dict_new_names, inplace=True)
    df_temp = df_temp[list(dict_new_names.values())]
    # store the data in a dictionary
    dict_of_dfs[file] = df_temp

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# set up a database
engine_one = sa.create_engine("mysql+mysqldb://root:pass@localhost/")
connection_one = engine_one.connect()
# create a database
command_temp = "CREATE DATABASE IF NOT EXISTS my_db;"
connection_one.execute(command_temp)
# create a new user & grant privileges
command_temp = "CREATE USER IF NOT EXISTS 'sample_user'@'localhost' IDENTIFIED BY 'pass1234';"
connection_one.execute(command_temp)
command_temp = "GRANT ALL ON my_db.* TO 'sample_user'@'localhost';"
connection_one.execute(command_temp)
connection_one.close()
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# load the data using to_sql command
engine_two = sa.create_engine("mysql+mysqldb://sample_user:pass1234@localhost/my_db")
connection_two = engine_two.connect()

dict_of_types = {"date": sa.DATE, "open": sa.FLOAT(10, 2),
                 "close": sa.FLOAT(10, 2), "high": sa.FLOAT(10, 2),
                 "low": sa.FLOAT(10, 2)}
dict_of_tables_names = dict(zip(dict_of_dfs.keys(), ['SPX', 'OIL', 'USDJPY']))

for iter_key, iter_val in dict_of_dfs.items():
    iter_val.to_sql(con=connection_two, dtype=dict_of_types,
                    index=False, name=dict_of_tables_names[iter_key])

# drop the tables to free the space
for iter_key in dict_of_tables_names.values():
    temp_cmd = "DROP TABLE IF EXISTS " + iter_key + ";"
    connection_two.execute(temp_cmd)
connection_two.close()
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# load the data row-by-row using SQLAlchemy's insert()
# command_temp = "CREATE USER IF NOT EXISTS 'sample_user'@'localhost' IDENTIFIED BY 'pass1234';"

dict_of_dfs.keys()
df1 = dict_of_dfs["usdjpy_d.csv"]
df1.head()
df1.melt()
# melt all the data frames (transform them into long format)
for iter_key, iter_val in dict_of_dfs.items():
    df_temp = dict_of_dfs[iter_key]
    df_temp.reset_index(drop=False, inplace=True)
    df_temp = df_temp.melt(id_vars="index", value_vars=["date", "open", "close", "high", "low"],
                           var_name="var_col", value_name="value_col")
    dict_of_dfs[iter_key] = df_temp.copy()
list_of_dfs = list(dict_of_dfs.values())
df_full = pd.concat(objs=list_of_dfs, axis=0)
df_full.reset_index(inplace=True, drop=True)

engine_three = sa.create_engine("mysql+mysqldb://sample_user:pass1234@localhost/my_db")
connection_three = engine_three.connect()

df_full.head()

metadata_three = sa.MetaData(bind=engine_three)
target_table = sa.Table("sample_table", metadata_three,
                        sa.Column("index", sa.BIGINT, nullable=True, autoincrement=True),
                        sa.Column("var_col", sa.VARCHAR(20), nullable=False),
                        sa.Column("value_col", sa.VARCHAR(20), nullable=False)
                        )
metadata_three.create_all()

for iter_num, iter_row in df_full.iterrows():
    iter_ins = target_table.insert().values(var_col=iter_row["var_col"],
                                            value_col=iter_row["value_col"])
    connection_three.execute(iter_ins)

connection_three.close()

# ----------------------------------------------------------------------------------------------------------------------
