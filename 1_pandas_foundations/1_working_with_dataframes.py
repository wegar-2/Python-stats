# 0. libraries' imports
import numpy as np
import pandas as pd
import sys
import os
import string
import random

# 1. creating DataFrames
np.random.seed(seed=123456)
N = 200
vec1 = np.random.randn(N)
vec2 = np.random.randint(low=0, high=10, size=N)
vec3 = np.random.gamma(shape=5, scale=5, size=N)
vec4 = np.random.chisquare(df=20, size=N)
vec5 = np.random.randint(low=0, high=4, size=N)

# 1.1. sampling from a list in Python - using numpy
my_letters = np.array(list(string.ascii_lowercase))
my_letters = np.array(my_letters[0:10])
vec2 = my_letters[list(vec2)]

my_countries = np.array(["USA", "China", "Russia", "Japan", "Germany"])
vec5 = my_countries[vec5]

# 1.2. Two ways of creating the pandas DataFrame

# 1.2.1.
df1 = pd.DataFrame(data={"categ_A": vec2, "country": vec5, "var_X": vec1, "var_Y": vec3, "var_Z": vec4})
df1.head(3)

# 1.2.2.
# concatenate vertically
data1 = np.concatenate((vec2.reshape(N, 1), vec5.reshape(N,1), vec1.reshape(N, 1),
                                vec3.reshape(N, 1), vec4.reshape(N, 1)), axis=1)
df2 = pd.DataFrame(data=data1, columns=["categ_A", "country", "var_X", "var_Y", "var_Z"])
df2.head(3)

# 2. performing analysis by a group

# 2.1. default call
df1_gpd = df1.groupby(by="categ_A")
df1_gpd.sum() # note that column "country" is not in result
df1_gpd.min() # here, column "country" is in the results set
df1_gpd.max()

# 2.2. perform grouping using selected columns
df1_num = df1.loc[:, ["country", "var_X", "var_Y", "var_Z"]]
df1_num.groupby(by="country").sum()

# 2.3. renaming pd.DataFrame's columns
df1.rename(columns={"country": "State"}, inplace=True)
df1.head(3)

# 2.4. select all columns but one selected
# 2.4.1. build a data frame with a lot of columns
nums = np.random.randint(low=1, high=11, size=100)

# 2.5. select all columns that start with a specific pattern

# 3. performing analyses by multiple groups
