### HOW TO MANUALLY INSERT ROWS INTO EXISTING TABLES ###

# 1. First, let's create a simple table
drop table if exists time_series.test_table;

create table if not exists time_series.test_table (
	date_col DATE,
    value_col DECIMAL(10, 2)
);

# 2. Now, insert some rows into the table
INSERT INTO time_series.test_table(date_col, value_col) VALUES ("2016-10-13", 123.23);
INSERT INTO time_series.test_table(date_col, value_col) VALUES ("2017-02-11", 75422.12);

# 3. Check whether the rows were actually put into the table
SELECT * FROM time_series.test_table;
