import numpy as np


### 1. Basics of vectors
# create two vectors to start with
vec1 = np.random.randn(10)
vec2 = np.random.gamma(scale=3, shape=4, size=10)

# concatenate vectors vec1 & vec2 vertically
print(vec1)
vec1.shape = (10, 1)
print(vec1)
vec1.shape = (1, 10)
print(vec1)
vec2.shape = (10, 1)
vecs_cntnd = np.concatenate((vec1, vec2), axis=1)
print(vecs_cntnd)
print(vecs_cntnd.shape)

# concatenate vectors vec1 & vec2 horizontally
vec1 = vec1.shape(1, 10)
vec2 = vec2.shape(1, 10)
vecs_cntnd2 = np.concatenate((vec1, vec2), axis=0)
print(vecs_cntnd2)
print(vecs_cntnd2.shape)

# create two random matrices
mat1 = np.random.randint(low=1, high=11, size=(2, 4))
mat2 = np.random.randint(low=1, high=11, size=(4, 3))

# stack a long vector into matrix in a specific way
longvec = np.random.randint(low=1, high=11, size=40)
np.reshape(a=longvec, order=0, )

### 2. matrices multiplication
mat3 = np.dot(a=mat1, b=mat2)
print(mat3.shape)


### 3. basic eigenanalysis
mat_test = np.random.randint(low=-10, high=11, size=(4, 4))
# a - eigenvalues
# b - eigenvectors corresponding to these eigenvalues
(a, b) = np.linalg.eig(mat_test)


### 4. Hadamard product (elementwise multiplication)
 np.multiply(x1=, x2=)