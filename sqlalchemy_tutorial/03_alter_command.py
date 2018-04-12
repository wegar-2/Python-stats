import sqlalchemy as sa

# create a connection
engine1 = sa.create_engine("mysql://test_user:test1234@localhost/test_db")
connection1 = engine1.connect()

# create a table
metadata = sa.MetaData(engine1)

table1 = sa.Table("table_2", metadata,
                  sa.Column('my_date_column', sa.DATE),
                  sa.Column('my_int_column', sa.INT),
                  sa.Column('my_float_column', sa.FLOAT),
                  sa.Column('another_int_column', sa.INT)
                  )

metadata.create_all(tables=[table1])
metadata.reflect(bind=engine1)
metadata.tables.keys()
