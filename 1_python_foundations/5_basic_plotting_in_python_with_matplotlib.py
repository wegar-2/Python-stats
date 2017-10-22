import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string

# fix the random seed
np.random.seed(seed=9070)

# Making sure that data will be accessed appropriately
print("Current directory: ", os.getcwd())
os.chdir()

### 1. Very simple linear plot - a guide through various plot elements
my_letters = list(string.ascii_uppercase)
vec1 = np.random.randn(len(my_letters))
df1 = pd.DataFrame(data=vec1, columns=["variable_X"])
df1.head(5)

# 1.1. create the plot object
linear_plot = plt.figure(1)
# 1.2. add the plot axes - one plane in this case
lp_ax1 = linear_plot.add_subplot(1, 1, 1)
# 1.3. produce the plot
lp_ax1.plot(df1.loc[:, "variable_X"], linewidth=2, color="red")
# 1.4. set the ticks and tick labels on the horizontal axis
lp_ax1.set_xticks(np.arange(0, len(my_letters), 1))
lp_ax1.set_xticklabels(my_letters)
# 1.5. set the ticks and tick labels on the vertical axis
lp_ax1.set_yticks(np.linspace(start=np.min(vec1)*1.1, stop=np.max(vec1)*1.1, num=20))
# enable the grid
lp_ax1.grid(True)
# 1.6. set the plot title
lp_ax1.set_title("Sample linear plot", fontsize=26)
# 1.7. set the axes' titles
lp_ax1.set_xlabel("My customized letter labels", fontsize=18)
lp_ax1.set_ylabel("Gaussian noise", fontsize=18)

# sidenote: np.linspace vs. np.arange
ar = np.arange(start=0, stop=1, step=0.01)
ls1 = np.linspace(start=0.01, stop=1, num=100)

### 3. Very simple EAD of financial data
# 3.1. load the data
my_dir = "/Python-stats/data/ng_f_d.csv"
data_dir = os.path.split(os.getcwd())[0] + my_dir
data1 = pd.read_csv(data_dir)
data1 = data1.loc[:, ["Data", "Zamkniecie"]]
data1.rename(columns={"Data": "date", "Zamkniecie": "close"}, inplace=True)
# 3.2. produce the series of log-return
data1.loc[:, "lr"] = np.log(data1.loc[:, "close"]/data1.loc[:, "close"].shift(1))

# 3.3. First plot: simple line plot of the returns
lr_fig = plt.figure(2)
lr_ax = lr_fig.add_subplot(1, 1, 1)
lr_ax.plot(data1.loc[:, "lr"], color="red", alpha=0.4)
lr_ax.set_xticks(np.arange(start=0, stop=len(data1.loc[:, "lr"]), step=250))
m, M = np.min(data1.loc[:, "lr"]), np.max(data1.loc[:, "lr"])
m = round(m, ndigits=2)
M = round(M, ndigits=2) + 0.01
lr_ax.set_yticks(np.arange(start=-0.35, stop=0.35, step=0.05))
lr_ax.grid(True)
lr_ax.set_title("Log-return of the futures price of natural gas at NYMEX", fontsize=25)
lr_ax.set_xlabel("Consecutive trading day", fontsize=18)
lr_ax.set_ylabel("Daily log-return of the price", fontsize=18)

# 3.4. Second plot: histogram of log returns
data2 = data1.dropna(subset={"lr"})
hist_fig = plt.figure(1)
hist_ax = hist_fig.add_subplot(1, 1, 1)
hist_ax.hist(data2.loc[:, "lr"], normed=True, bins=100,
             edgecolor="black", linewidth=1.6, color="blue",
             alpha=0.24)
hist_ax.grid(True)
# calculate basic statistics and overlay on the plot
mean_hat = np.mean(data2.loc[:, "lr"])
sigma_hat = np.std(data2.loc[:, "lr"])
hist_ax.axvline(mean_hat, color="red", linewidth=2) # overlay the mean value
hist_ax.axvline(mean_hat+sigma_hat, color="blue", linewidth=2, linestyle="dashed")
hist_ax.axvline(mean_hat-sigma_hat, color="blue", linewidth=2, linestyle="dashed")

# 3.5. carry out Kolmogorov-Smirnov test for normality
# 3.6. carry out Kolmogorov-Smirnov test for t-Student distribution
# 3.7. carry out Shapiro-Wilk test for normality
# 3.8. carry out the Anderson-Darling test for normality
# 3.9. carry out Jarque-Bera normality test

