import numpy as np
import pandas as pd
# import math
import matplotlib.pyplot as plt
import sys
import os
import pickle


np.random.seed(seed=908071)

# ----------------------------- 1. Generating a simple dataset that will be used ------------------------------------- #
N = 1000
sigma = 2 # standard deviation of the dependent variable
beta_0 = 5 # intercept
beta_1 = 5
beta_2 = 7
beta_3 = 0.55
# 1.1. explanatory variables
x_0 = np.ones(N).reshape(N, 1) # vector of ones, for the intercept
x_1 = np.random.uniform(low=0, high=10, size=N).reshape(N, 1)
x_2 = np.random.uniform(low=1, high=6, size=N).reshape(N, 1)
x_3 = np.random.gamma(shape=5, scale=20, size=N).reshape(N, 1)
error_term = np.random.rand(N)*sigma
# 1.2. dependent variable
betas = np.array([beta_0, beta_1, beta_2, beta_3]).reshape([4, 1])
X = np.concatenate((x_0, x_1, x_2, x_3), axis=1)
error_term = error_term.reshape(N, 1)
y = np.dot(X, betas) + error_term
# 1.3. Putting it all together into a nice dataframe
# 1.3.1. squeeze vectors because they will not be accepted as input otherwise
y = np.squeeze(y, axis=1)
x_1 = np.squeeze(x_1, axis=1)
x_2 = np.squeeze(x_2, axis=1)
x_3 = np.squeeze(x_3, axis=1)
# 1.3.2. make the data frame
df_data = pd.DataFrame(data={"dep_var": y, "var_1": x_1, "var_2": x_2, "var_3": x_3})
# 1.4. saving the data into a file and loading from the file
# 1.4.1. save to
file_to_save_to = os.path.join(os.getcwd(), "asdf.p")
file1 = open(file=file_to_save_to, mode="wb")
pickle.dump(file=file1, obj=df_data)
file1.close()
# 1.4.2. load from
del df_data
file1 = open(file=file_to_save_to, mode="rb")
df_data = pickle.load(file=file1)
file1.close()
df_data.rename(columns={"dep_var": "y", "var_1": "x1", "var_2": "x2", "var_3": "x3"}, inplace=True)

# 1.5. basic visualizations of the dataset
# 1.5.1. histograms: one plot with subplots
fig_hists = plt.figure(1)
# upper left: y
hist_ul = fig_hists.add_subplot(2, 2, 1)
hist_ul.grid(True, alpha=0.4)
hist_ul.hist(x=df_data.loc[:, "y"], normed=True, color="blue",
             edgecolor="black", linewidth=1.4, alpha=0.5, bins=40)
hist_ul.set_title(label="Histogram for dependent variable", fontsize=22)
hist_ul.set_xlabel("Value of the dependent variable", fontsize=17)
hist_ul.set_ylabel("Share for a bin", fontsize=17)
# upper right: x1
hist_ur = fig_hists.add_subplot(2, 2, 2)
hist_ur.hist(x=df_data.loc[:, "x1"], normed=True, color="red",
             edgecolor="black", linewidth=1.4, alpha=0.5, bins=40)
hist_ur.set_title(label="Histogram for 1st explanatory variable", fontsize=22)
hist_ur.set_xlabel("Value of the explanatory variable", fontsize=17)
hist_ur.set_ylabel("Share for a bin", fontsize=17)
# lower left: x2
hist_ll = fig_hists.add_subplot(2, 2, 3)
hist_ll.hist(x=df_data.loc[:, "x2"], normed=True, color="green",
             edgecolor="black", linewidth=1.4, alpha=0.5, bins=40)
hist_ll.set_title(label="Histogram for 2nd explanatory variable", fontsize=22)
hist_ll.set_xlabel("Value of the explanatory variable", fontsize=17)
hist_ll.set_ylabel("Share for a bin", fontsize=17)
# lower right: x3
hist_lr = fig_hists.add_subplot(2, 2, 4)
hist_lr.hist(x=df_data.loc[:, "x3"], normed=True, color="grey",
             edgecolor="black", linewidth=1.4, alpha=0.5, bins=40)
hist_lr.set_title(label="Histogram for 3rd explanatory variable", fontsize=22)
hist_lr.set_xlabel("Value of the explanatory variable", fontsize=17)
# handle the overlaying texts on subplots' labels
fig_hists.autofmt_xdate() # not perfect...

# 1.5.2. scatter plots of explanatory vs dependent variables
# 1.5.2.1.
fig_sp = plt.figure(num=2)
ax1 = fig_sp.add_subplot(3, 1, 1)
ax1.scatter(x=df_data.loc[:, "x1"], y=df_data.loc[:, "y"], color="red")
ax1.grid(True)
ax1.set_title(label="Scatter plot, dependent vs first explanatory")
# 1.5.2.2.
ax2 = fig_sp.add_subplot(3, 1, 2)
ax2.scatter(x=df_data.loc[:, "x2"], y=df_data.loc[:, "y"], color="blue")
ax2.grid(True)
ax2.set_title(label="Scatter plot, dependent vs second explanatory")
# 1.5.2.3.
ax3 = fig_sp.add_subplot(3, 1, 3)
ax3.scatter(x=df_data.loc[:, "x3"], y=df_data.loc[:, "y"], color="green")
ax3.grid(True)
ax3.set_title(label="Scatter plot, dependent vs third explanatory")

# 1.5.3. 3D scatter plots of pairs of explanatory variables vs dependent variable


# 1.6. workaround to make the dataframe without squeezing vectors