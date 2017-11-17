# ----------------------------------------------------------------------------------------------------------------------
# 0. libraries' imports
import numpy as np
import pandas as pd
import sys
import os
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


# ----------------------------------------------------------------------------------------------------------------------
# 5. sorting a DataFrame with a MultiIndex


# 5.1. preliminaries: sorting a DataFrame with one-level index only
df1 = pd.read_csv(filepath_or_buffer=os.path.join(os.getcwd(), "data", "ng_f_d.csv"), sep=",", index_col=[0])
# 5.1.1. sidenote: sampling from a pandas.DataFrame
df2 = df1.sample(n=1000, axis=0, replace=False)

# 5.2. sort by index
df3 = df2.sort_index(axis=0, level=0)

# 5.3. sort by a column
df4 = df2.sort_values(by=["Zamkniecie"], ascending=[1])
print(df4.head(5))
print(df4.tail(5))


# 5.2. sorting a DataFrame with MultiIndexes
list1 = [str(el) for el in list(string.ascii_lowercase[0:10])]
list2 = ["group_" + str(k+1) for k in range(4)]
mi_r = pd.MultiIndex.from_product(iterables=(list2, list1),
                                  names=["group", "subgroup"])
mi_c = pd.MultiIndex.from_product(iterables=(("X", "Y"), ("country_1", "country_2", "country_3")),
                                  names=["category", "country"])
df_with_mi = pd.DataFrame(data=np.random.gamma(shape=5, scale=5, size=[40, 6]),
                          columns=mi_c, index=mi_r)
print(df_with_mi)
# 5.2. sorting in groups on the first level of columns
df_s1 = df_with_mi.sort_index(by=("X", "country_1"), ascending=False)


# ----------------------------------------------------------------------------------------------------------------------
# 6. Walk through some useful (in the context of MultiIndexes on DataFrames) pandas functions
list1 = ["a", "b"]
list2 = ["subgroup_" + str(el+1) for el in range(10)]
mi_r = pd.MultiIndex.from_product(iterables=(list1, list2), names=["letter", "subgroup"])
list1 = ["a", "b"]
list2 = ["subgroup_1", "subgroup_2"]
mi_c = pd.MultiIndex.from_product(iterables=(list1, list2), names=["level_1", "level_2"])
df_test = pd.DataFrame(data=np.random.randn(20, 4), columns=mi_c, index=mi_r)
# 6.0.1. Sidenote: swapping indexes
my_cmi = pd.MultiIndex.from_product(iterables=(["a", "b"], ["Q", "P"]), names=["col_lev_1", "col_lev_2"])
my_rmi = pd.MultiIndex.from_product(iterables=(["A", "B"], ["X", "Y", "Z", "U"]), names=["row_lev_1", "row_lev_2"])
my_df = pd.DataFrame(data=np.random.randn(8, 4), columns=my_cmi, index=my_rmi)
# swap MultiIndex on columns
my_df_c = my_df.swaplevel(axis=0, i=0, j=1)
my_df_c.sort_index(level=0, axis=0, inplace=True)
# swapMultiIndex on rows
my_df_r = my_df.swaplevel(axis=1, i=0, j=1)
my_df_r.sort_index(level="col_lev_2", axis=1, inplace=True)
# NOTE: remeber to apply the sort_index function on a DataFrame to order the indexes


# 6.1. pandas.DataFrame.reset_index
# 6.1.1. dropping all levels of indexes
df_test2 = df_test.reset_index(level=["letter", "subgroup"], inplace=False, drop=False)
# 6.1.2. dropping one level of indexes
df_test3 = df_test.reset_index(level="letter", inplace=False, drop=False)


# 6.2. pandas.DataFrame.sort_index: as mentioned earlier, sort_index is used to sort MultiIndex on columns or rows at
#  one of the MultiIndex levels
df_test = df_test.columns.droplevel(level=0)
df_test4 = df_test.copy()
df_test4.columns = df_test4.columns.droplevel(level=0)


# 6.4. pandas.DataFrame.sort_values
col_mi = pd.MultiIndex.from_product(iterables=(["A", "B"], ["x", "y"]))
row_mi = pd.MultiIndex.from_product(iterables=(["Germany", "France"], ["a", "b", "c", "d", "e"]))
df_ung = pd.DataFrame(data=np.random.randn(10, 4), index=row_mi, columns=col_mi)
# sorting
df_ung.sort_values(by=("A", "x"))


# 6.3.pandas.DataFrame.groupby
# 6.3.1. sort by a column in subgroups
my_letters = np.random.choice(a=["a", "b", "c"], p=[0.25, 0.25, 0.5], replace=True, size=1000)
my_letters = pd.DataFrame(data={"col1": my_letters})
gp1 = my_letters.groupby(by="col1")
gp1.size()
# 6.3.2.
data1 = np.random.randn(1000, 4)
data2 = np.random.choice(a=["a", "b", "c", "d"], p=[0.5, 0.2, 0.2, 0.1], replace=True, size=1000).reshape(1000, 1)
data3 = np.concatenate((data1, data2), axis=1)
array1 = np.array(["my_group", "A", "A", "B", "B"])
array2 = np.array(["my_group", "X", "X", "Y", "Y"])
mi_c = pd.MultiIndex.from_arrays(arrays=(array1, array2), names=[])
tuple_1 = tuple(string.ascii_lowercase[0:20])
tuple_2 = tuple([str(k+1) for k in range(50)])
mi_r = pd.MultiIndex.from_product(iterables=(tuple_1, tuple_2), names=[])
df1 = pd.DataFrame(data=data3, columns=mi_c, index=mi_r)
df2 = df1.reset_index(level=[0, 1], inplace=False, drop=False)
df2.head(10)
gpd1 = df2.groupby(by="level_0")
sorted1 = gpd1.sort_values(by=["A", "X"])

# ----------------------------------------------------------------------------------------------------------------------
# 7. Pivoting DataFrames


# 7.1. Pivoting data frame with one-level index


# 7.2. Pivoting data frame with multi-level indexes


