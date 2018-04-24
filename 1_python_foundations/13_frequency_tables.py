# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# WALK THROUGH THE TUTORIAL: http://hamelg.blogspot.com/2015/11/python-for-data-analysis-part-19_17.html
# ----------------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import os
import string

# ----------------------------------------------------------------------------------------------------------------------
data1 = pd.read_csv(filepath_or_buffer=os.path.join(os.getcwd(), "data", "train.csv"))
cabin_col = data1.loc[:, "Cabin"].astype(str)
data1.head()
data1.apply(axis=0, func = lambda x: len(set(list(x))))

# ----------------------------------------------------------------------------------------------------------------------
# 1-way tables
survived_1dim = pd.crosstab(index=data1.loc[:, "Survived"], columns="a")
parch_1dim = pd.crosstab(index=data1.loc[:, "Parch"], columns="parch")

# ----------------------------------------------------------------------------------------------------------------------
# 2-way tables


# ----------------------------------------------------------------------------------------------------------------------
list1 = list(string.ascii_lowercase[0:10])
list2 = list(string.ascii_lowercase[10:20])
list3 = ["000", "999"]
mi1 = pd.MultiIndex.from_product(iterables=[list1, list3])
mi2 = pd.Index(list2)
df1 = pd.DataFrame(index=mi1, columns=mi2, data=np.random.gamma(shape=5, scale=5, size=[20, 10]))

df1.reset_index(level=[0, 1], drop=False, inplace=True)
print(df1.columns)
tab1 = pd.crosstab(index=df1.loc[:, "level_0"], columns=df1.loc[:, "level_1"], aggfunc=np.sum, values=df1.loc[:, "k"])

df2 = pd.DataFrame(data={"col1": np.random.randint(low=1, high=11, size=1000)})
tab2 = pd.crosstab(index=df2.loc[:, "col1"], columns="my_count")

my_colnames = list(string.ascii_lowercase[0:20])
df3 = pd.DataFrame(columns=my_colnames, data=np.random.normal(loc=0, scale=1, size=[1000, 20]))
df3.reset_index(level=0, inplace=True, drop=False)
df4 = df3.melt(id_vars="index", value_vars=list(string.ascii_lowercase[0:20]),
               var_name="var_name_col", value_name="value_col")
df5 = df4.copy()
df5.loc[:, "group"] = ["a" if el in list(string.ascii_lowercase[0:10]) else "b" for el in df5.loc[:, "var_name_col"]]
df5.head()
tab1 = pd.crosstab(index=df5.loc[:, "group"], columns="count")
fractions1 = tab1/tab1.loc[:, "count"].sum() # fractions

df5.head()
tab2 = pd.crosstab(index=df5.loc[:, "var_name_col"], columns=df5.loc[:, "group"])



# ----------------------------------------------------------------------------------------------------------------------
# yet another exercise...

