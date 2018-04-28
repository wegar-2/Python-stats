# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# WALK THROUGH THE TUTORIAL: http://hamelg.blogspot.com/2015/11/python-for-data-analysis-part-19_17.html
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import os
import string
import datetime

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
# working with dates and time series -----------------------------------------------------------------------------------
start_date = datetime.date(year=2001, month=1, day=1)
end_date = datetime.date(year=2015, month=12, day=31)

timestamp_start = pd.Timestamp(start_date)
timestamp_end = pd.Timestamp(end_date)

# data range - daily frequency
dr_daily = pd.date_range(start=timestamp_start, end=end_date, freq="D")

# data range - business day frequency
dr_business_day = pd.date_range(start=timestamp_start, end=timestamp_end, freq="B")

# joining two time series
data1 = pd.DataFrame(index=dr_daily, data={"ts_1": np.random.randn(len(dr_daily))})
data2 = pd.DataFrame(index=dr_business_day, data={"ts_2": np.random.gamma(shape=1, scale=3,
                                                                          size=len(dr_business_day))})
data_mgd = pd.merge(left=data1, right=data2, left_index=True, right_index=True, how="left")
print(data_mgd.isnull().sum(axis=0))
data_mgd.fillna(method="ffill", inplace=True)


# ----------------------------------------------------------------------------------------------------------------------
# pandas' groupby vs crosstab
col1 = np.random.randn(10000)
col2 = np.random.randn(10000)
group_1 = np.random.choice(a=list(string.ascii_uppercase[0:20]), size=10000, replace=True)
group_2 = np.random.choice(a=[str(el) for el in range(10)], size=10000, replace=True)
df1 = pd.DataFrame(data={"var_X": col1, "var_Y": col2, "group1": group_2, "group2": group_1})
df1.head()

# grouping using groupby
summ1 = df1.groupby(by=["group1", "group2"]).count()
summ1.reset_index(drop=False, inplace=True)
summ1.head()
df1.pivot_table()
summ2 = summ1.pivot_table(index="group2", values=["var_X", "var_Y"], columns="group1")

# grouping using pandas' crosstab
tab1 = pd.crosstab(index=df1.loc[:, "group2"], columns=df1.loc[:, "group1"],
                   values=df1.loc[:, "var_X"], aggfunc=np.sum)
# ----------------------------------------------------------------------------------------------------------------------
