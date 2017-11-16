# ----------------------------------------------------------------------------------------------------------------------
# 0. libraries' imports
import numpy as np
import pandas as pd
# import sys
# import os
import string
# import random
import itertools


# ----------------------------------------------------------------------------------------------------------------------
# 1. creating DataFrames
np.random.seed(seed=123456)
N = 200
vec1 = np.random.randn(N)
vec2 = np.random.randint(low=0, high=10, size=N)
vec3 = np.random.gamma(shape=5, scale=5, size=N)
vec4 = np.random.chisquare(df=20, size=N)
vec5 = np.random.randint(low=0, high=4, size=N)


# 1.1. sampling

# 1.1.1. sampling from a list in Python - using numpy
my_letters = np.array(list(string.ascii_lowercase))
my_letters = np.array(my_letters[0:10])
vec2 = my_letters[list(vec2)]
my_countries = np.array(["USA", "China", "Russia", "Japan", "Germany"])
vec5 = my_countries[vec5]

# 1.1.2. sampling using numpy's built-in function numpy.random.choice
popul = ["a", "b", "c", "e", "f", "q"]
sample_from_popul = np.random.choice(a=popul, replace=True, size=1000)


# 1.2. Two ways of creating the pandas DataFrame

# 1.2.1. create DataFrame passing dictionary as 'data' parameter
df1 = pd.DataFrame(data={"categ_A": vec2, "country": vec5, "var_X": vec1, "var_Y": vec3, "var_Z": vec4})
df1.head(3)

# 1.2.2.
# concatenate numpy ndarrays vertically
data1 = np.concatenate((vec2.reshape(N, 1), vec5.reshape(N,1), vec1.reshape(N, 1),
                                vec3.reshape(N, 1), vec4.reshape(N, 1)), axis=1)
df2 = pd.DataFrame(data=data1, columns=["categ_A", "country", "var_X", "var_Y", "var_Z"])
df2.head(3)

# 1.2.3.


# ----------------------------------------------------------------------------------------------------------------------
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


# ----------------------------------------------------------------------------------------------------------------------
# 3. performing analyses by multiple groups


# ----------------------------------------------------------------------------------------------------------------------
# 4. pandas' MultiIndexes


# 4.1. Three ways of creating a MultiIndex object

# 4.1.1. pd.MultiIndex.from_arrays
my_countries = ["Germany", "France", "Netherlands", "Italy", "Poland"]
my_groups = list(string.ascii_lowercase[0:8])
cartesian_product = list(itertools.product(my_countries, my_groups))
array1 = [el[0] for el in cartesian_product]
array2 = [el[1] for el in cartesian_product]
test_mi_1 = pd.MultiIndex.from_arrays(arrays=[array1, array2])
# 4.1.1.1. sidenote on unpacking 3-tuples (n-tuples in general)
list1 = ["a", "b", "c"]
list2 = list(range(4))
list3 = ["level_1", "level_2"]
list_of_tuples = list(itertools.product(list1, list2, list3))
# unpacking using zip(*iterables)
list_out_1, list_out_2, list_out_3 = zip(*list_of_tuples)

# 4.1.2. pd.MultiIndex.from_product: pass iterables that are used to make Cartesian product of them
list1 = list(string.ascii_lowercase[0:10])
list2 = [str(el) for el in list(range(3))]
test_mi_2 = pd.MultiIndex.from_product(iterables=(list1, list2))

# 4.1.3. pd.MultiIndex.from_tuples
tuple1 = ("Poland", "Czech Republic", "Slovakia", "Lithuania", "Belarus")
tuple2 = ("a", "b", "c")
test_mi_3 = pd.MultiIndex.from_tuples(tuples=(tuple1, tuple2))


# 4.2. pandas' multiindex on columns and rows

# 4.2.1. MultiIndex on rows
# 4.2.1.1. input data
col_1 = np.random.gamma(shape=5, scale=4, size=300).reshape(300, 1)
col_2 = np.random.chisquare(df=20, size=300).reshape(300, 1)
col_3 = np.random.uniform(low=30, high=100, size=300).reshape(300, 1)
my_numbers = np.concatenate((col_1, col_2, col_3), axis=1)
# 4.2.1.2. create multiindex and make a DataFrame
start_date = pd.Timestamp("2012-01-01")
end_date = pd.Timestamp("2015-12-12")
dr1 = list(pd.date_range(start=start_date, end=end_date, freq="d"))
list_of_days = np.random.choice(a=dr1, replace=False, size=100)
list_of_countries = ["Russia", "China", "USA"]
mi1 = pd.MultiIndex.from_product((list_of_countries, list_of_days), names=["country", "date"])
# not that the dataframe below is not sorted by date
df_mi_1 = pd.DataFrame(data=my_numbers, index=mi1, columns=["X", "Y", "Z"])

# 4.2.2. MultiIndex on columns
data2 = np.random.randn(7,4)
mi2 = pd.MultiIndex.from_product(iterables=(["a", "b"], ["group_1", "group_2"]), names=["letter", "group"])
df_mi_2 = pd.DataFrame(data=data2, columns=mi2)


# 4.3. accessing elements of DataFrame with a MultiIndex

# 4.3.1. extracting one group on the second level
print(df_mi_2.loc[:, (slice(None), "group_2")])
# 4.3.2. extracting on first level: note the difference between the two calls below
print(df_mi_2.loc[:, ("a", slice(None))])
print(df_mi_2.loc[:, "a"]) # this call might be ambiguous
# 4.3.2.1. Remedy for the ambiguity in 4.3.2. above: use .xs call on a DataFrame with MultiIndex
mi_columns = pd.MultiIndex.from_product(iterables=(["a", "b", "c", "d"], ["group1", "group2"]))
mi_rows = pd.MultiIndex.from_product(iterables=([str(el) for el in range(10)], ["Germany", "Austria", "Italy",                                                                          "Switzerland"]))
df_test = pd.DataFrame(data=np.random.randn(40, 8),
                       columns=mi_columns, index=mi_rows)
# accessing data: columns
print(df_test.xs("a", axis=1, level=0))
print(df_test.xs("group2", axis=1, level=1))
# accessing data: rows
print(df_test.xs("Germany", axis=0, level=1))
print(df_test.xs("5", axis=0, level=0))


# 4.4. sorting a DataFrame with a MultiIndex

# 4.4.1. preliminaries: sorting a DataFrame with one-level index only

# 4.4.2. sorting a DataFrame with MultiIndexes


# ----------------------------------------------------------------------------------------------------------------------
# 5.
