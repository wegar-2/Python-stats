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
longvec2 = np.reshape(a=longvec, order='C', newshape=(5, 8)) # stack elements of longvec into rows
longvec3 = np.reshape(a=longvec, order='F', newshape=(5, 8)) # stack elements of longvec into columns

### 2. matrices multiplication
mat3 = np.dot(a=mat1, b=mat2)
print(mat3.shape)


### 3. basic eigenanalysis
mat_test = np.random.randint(low=-10, high=11, size=(4, 4))
# a - eigenvalues
# b - eigenvectors corresponding to these eigenvalues
(a, b) = np.linalg.eig(mat_test)


### 4. Hadamard product (elementwise multiplication)
first_vec = np.random.randint(low=1, high=11, size=20)
first_mat = np.reshape(a=first_vec, order="C", newshape=(5, 4))
second_vec = np.random.randint(low=1, high=11, size=20)
second_mat = np.reshape(a=second_vec, order="F", newshape=(5, 4))
had_res = np.multiply(first_mat, second_mat) # element-by-element multiplication

### 5. Creating a matrix of ones
mat_ones = np.ones(shape=(5, 5))

### 6. Creating a diagonal matrix from a vector (its elements are put on the diagonal)
mat_diag = np.diag(v=np.ones(shape=6))

### 7. numpy.squeeze
vec1 = np.random.randn(100)
vec1 = vec1.reshape(100, 1)
vec2 = np.squeeze(vec1, axis=1)
print(vec2.shape)
vec3 = vec1.reshape(1, 100)
vec4 = np.squeeze(vec3, axis=0)
print(vec4.shape)
# Note: the final result of squeezing both: (1, 100) and (100, 1) arrays is the same

### 8. numpy's outer function
vec1 = np.array([1, 2, 3, 4, 5])
vec2 = np.array([0, 1, 2, 3])
out = np.outer(a=vec1, b=vec2)