import sys
import os
import numpy as np
import pandas as pd
import sqlalchemy as sa

##############################################################################
##############################################################################
### NOTE: What is considered here is use of SQLAlchemy to connect       ######
###       to a MySQL database. It cannot be stressed enough that it is  ######
###       MYSQL DATABASE!!!                                             ######
##############################################################################
##############################################################################

#### It is assumed that MySQL Server is installed.
#### Moreover, there exists a user "test_user" who
#### has the requires access privileges to the DB
#### "time_series".
#### Port: 3306, password: _test_1_pass_2

# 1. Basic object - connection engine
connection_string = "mysql://test_user:_test_1_pass_2@localhost:3306/time_series"
con_engine = sa.create_engine(connection_string)