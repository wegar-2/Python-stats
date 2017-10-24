import numpy as np
import pandas as pd
import scipy.stats as spst
import matplotlib.pyplot as plt

np.random.seed(seed=102030)

## 1. NumPy stuff: algebra
vec1 = np.random.randint(low=-5, high=6, size=100)
vec1 = vec1.reshape(1, 100)
# by default, lines go into consecutive lines
mat1 = vec1.reshape(20, 5)
mat2 = vec1.reshape(10, 10)

# 1.1. matrix multiplication
matL = np.array([[1, 3, 2], [-1, 0, 2], [-4, 1, 2]])
matR = np.array([[10, -1, 0], [0, 5, 1], [3, 2, 4]])
matRes = np.dot(matL, matR) # dot can be memorized as the traditional notation of the traditional matrix product

# 1.2. Hadamard product
matL_H = np.random.randint(low=-4, high=5, size=[4, 6])
matR_H = np.random.randint(low=-4, high=5, size=[4, 6])
matRes_H = np.multiply(matL_H, matR_H)

# 1.3. reducing a dimension of ndarray


## 2. ScipyStats' first application: generating random numbers
chi2_obj = spst.chi2
chi2_obj.stats(df=10)

# 2.1. generic "normal distribution" object
normal_obj = spst.norm
normal_obj.ppf(0.5, loc=10, scale=2)
normal_obj.rvs(loc=10)

# 2.2. specific normal distribution object
normal_bj2 = spst.norm(loc=10, scale=2)
print("Check the median: ", normal_bj2.ppf(0.5))

## 3. Generating random numbers from a normal distribution
rnorm1 = spst.norm(loc=10, scale=2)
vec1 = rnorm1.rvs(size=10)

# stacking vectors into a matrix in numpy & scipy.stats only
norm_rg = spst.norm(loc=10, scale=3)
vecs_list = []
for k in range(100):
    vec = norm_rg.rvs(10).reshape(1, 10)
    vecs_list.append(vec)

vecs_tuple = tuple(vecs_list)
matrix1 = np.concatenate(vecs_tuple, axis=0)

## 4. Generating random sample from a chi-square distribution
chisq_object = spst.chi2(df=10)
vec_sample = chisq_object.rvs(size=1000)
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(1, 1, 1)
ax1.hist(x=vec_sample, color="blue", edgecolor="black",
         linewidth=1.5, alpha=0.5, bins=50, normed=True)
ax1.grid(True)
# overlay the density of the chisq
x_grid = np.linspace(start = min(vec_sample), stop=max(vec_sample), num=200)
y_vals = chisq_object.pdf(x_grid)
ax1.plot(x_grid, y_vals, color="red", linewidth=3)

## 5. generating random numbers from a t-Student distribution and overlaying density on the histogram
t_obj = spst.t(df=5)
t_sample = t_obj.rvs(size=1000)

fig2 = plt.figure(2)
ax2_upper_panel = fig2.add_subplot(2, 1, 1)
ax2_lower_panel = fig2.add_subplot(2, 1, 2)

# making a plot on the upper panel
ax2_upper_panel.hist(x=t_sample, color="red", alpha=0.35,
                     linewidth=1.5, edgecolor="black",
                     normed=True, bins=40)
M = max(abs(min(t_sample)), abs(max(t_sample)))
x_grid = np.linspace(start=-M, stop=M, num=200)
y_values = t_obj.pdf(x_grid)
ax2_upper_panel.plot(x_grid, y_values, linewidth=1.75, color="grey")

# making a plot on the lower panel
gamma_obj = spst.gamma(a=10)
# given the implementation, it is necessary to multiply by scale parameter to obtain random numbers from the
# two-parameters gamma distribution ("a" above is scale parameter
scale_param = 5
gamma_sample = scale_param*gamma_obj.rvs(size=1000)
ax2_lower_panel.hist(x=gamma_sample, color="blue", alpha=0.35,
                     linewidth=1.5, edgecolor="red",
                     normed=True, bins=40)
# add the density, too
x_grid = np.linspace(start=min(gamma_sample), stop=max(gamma_sample), num=200)
y_vals = gamma_obj.pdf(x_grid/scale_param)/scale_param
ax2_lower_panel.plot(x_grid, y_vals)
