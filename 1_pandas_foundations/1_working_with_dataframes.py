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
df1 = pd.DataFrame(data={"categ_A": vec2, "country": vec5, "var_X": vec1, "var_Y": vec3, "var_Z": vec4})
# df1.loc[0, "country"]
# df1.head(3)
# df1.dtypes



df1 = pd.DataFrame(data=[vec2, vec5, vec1, vec3, vec4],  ["categ_A", "country", "var_X", "var_Y", "var_Z"])