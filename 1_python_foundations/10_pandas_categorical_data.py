import string
import numpy as np
import pandas as pd


# 1. categorical data - creating a series with categorical data

# 1.1. directly during a series object creation
vec1 = np.random.choice(a=list(string.ascii_lowercase[0:20]), replace=True, size=1000).reshape(1000, 1)
vec1 = vec1.squeeze(axis=1)
pd.Series(data=vec1, dtype="category")

# 1.2. changing type of a pandas column to categorical
vec1 = np.random.randn(1000).reshape(1000, 1)
vec2 = np.random.gamma(scale=2, shape=3, size=1000).reshape(1000, 1)
vec3 = np.random.choice(a=list(string.ascii_lowercase), replace=True, size=1000).reshape(1000, 1)
vec4 = np.random.choice(a=list(string.ascii_uppercase), replace=True, size=1000).reshape(1000, 1)
my_array = np.concatenate((vec3, vec4, vec1, vec2), axis=1)

df1 = pd.DataFrame(data=my_array, columns=["categ_1", "categ_2", "var_1", "var_2"])
print(df1.dtypes)
dict_mapping = dict(zip(df1.columns.values, [str, str, float, float]))
df2 = df1.astype(dict_mapping)
print(df2.head())
print(df2.dtypes)


