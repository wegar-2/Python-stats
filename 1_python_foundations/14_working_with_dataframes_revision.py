import pandas as pd
import numpy as np
import string
import itertools

# 1. creating a dataframe
vec1 = np.random.randn(100)
vec2 = np.random.randint(low=1, high=101, size=100)
my_letters = list(string.ascii_uppercase[0:10])
vec3 = np.random.choice(a=my_letters, size=100, replace=True)

df1 = pd.DataFrame(data={"col1": vec1, "col2": vec2, "group": vec3})
df1.head()

df2 = df1.reset_index(level=0, inplace=False, drop=False)
print(df2.columns)
print(df2.head())

# 2. melting a data frame
df3 = pd.melt(frame=df2, id_vars=["index"], value_vars=["col1", "col2", "group"],
              value_name="value_column", var_name="which_variable")
df3.sort_values(by=["index", "which_variable"], inplace=True)
df3.reset_index(inplace=True, drop=True)
df3.head(10)

# dropping rows with character values
df4 = df3.loc[~df3.loc[:, "value_column"].isin(list(string.ascii_uppercase[0:10])), :]

# checking object types
print(df4.dtypes)
df5 = df4.copy()
df5.loc[:, "value_column"] = df4.loc[:, "value_column"].astype(np.float).copy()
print(df5.dtypes)

# 3. pivoting a data frame back to the entry form
df6 = df5.pivot_table(values="value_column", index="index", columns="which_variable")
df6.head(10)
del df1, df2, df3, df4, df5, df6
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


# sorting data frames by selected columns
df1 = pd.DataFrame(data={"col1": np.random.randn(100),
                         "col2": np.random.gamma(shape=5, scale=5, size=100)})
df1.head()

df2 = df1.sort_values(by="col1", ascending=True).copy()
df2.reset_index(drop=False, inplace=True)
df2.head()
del df1, df2

# multi-indexing
my_letters = list(string.ascii_lowercase[0:10])
my_digits = ["0", "1", "2"]
index1 = pd.MultiIndex.from_product(iterables=[my_letters, my_digits])
df1 = pd.DataFrame(index=index1, data={"col1": np.random.randn(30),
                                       "col2": np.random.randint(low=1, high=11, size=30)})
print(df1.head(6))

# swapping levels within a multiindex
df2 = df1.swaplevel(i=0, j=1, axis=0)
print(df2.head(7))
df3 = df2.sort_index(axis=0)

# swapping levels - general method (uses permutation on levels of an index)
list1 = list(itertools.product(["A", "B", "C"], ["0", "1", "2"]))
list1 = ["".join(el) for el in list1]
list2 = list(string.ascii_lowercase[0:10])
list3 = [str(el) for el in range(10)]
mi1 = pd.MultiIndex.from_product(iterables=[list1, list2, list3])

# getting a list of triples
list_of_index_values = list(itertools.product(list1, list2, list3))
print("How many numbers do I need?: ", len(list_of_index_values))

# extracting multiindex values at a specific level
mi1.get_level_values(level=0)

# creating another multiindex - this time for columns
list1 = ["China", "Russia", "USA"]
list2 = ["x", "y", "z", "v"]
mi2 = pd.MultiIndex.from_product(iterables=[list1, list2])

df4 = pd.DataFrame(index=mi1, columns=mi2, data=np.random.normal(loc=0, scale=1, size=[900, 12]))
df4.head()

# getting unique index value at various levels for rows' index:
index_rows = df4.index
print(type(index_rows))
print("level1: ")
print(set(index_rows.get_level_values(level=0)))
print("level2: ")
print(set(index_rows.get_level_values(level=1)))
print("level3: ")
print(set(index_rows.get_level_values(level=2)))

# rule: one slice for each multiindex level
df5 = df4.loc[(slice("A0", "C2"), slice(None), slice(None)), :]
df6 = df4.loc[(["A0", "C1"], ["b", "i"], slice(None)), :]
del df1, df2, df3, df4, df5, df6

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# summarizing variables by various groups








