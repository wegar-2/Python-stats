################################################################
################################################################
##### HOW TO: CREATE TABLES AND WHAT DATA TYPES THERE ARE ######
################################################################

# 1. create a simplest possible table
create table time_series.test_table (
	date1 DATE,
    variable1 float,
    variable float
);

# 2. different date and datetime formats
create table time_series.another_table (
	col_date DATE,
    col_datetime DATETIME,
    col_value FLOAT
);

# 3. Different floating value variables
create table time_series.test_table_2 (
	date1 DATE,
    var_1 FLOAT,
    var_2 DOUBLE,
    # DECIMAL(precision, scale):
    # 	precision - number of significant digits that are stored for values
    #			 	In short: precision is the total number of digits
    # 	scale - number of the digits stored after the decimal point
    decimal_1 DECIMAL(10, 2),
    # for instance DECIMAL(5,2) allows you to store 123.33 but not 12345.12
    decimal_2 DECIMAL(12, 4)
);

drop table time_series.test_table; 
drop table time_series.test_table_2;            
drop table time_series.another_table;