import numpy as np

# Create a NumPy 0-D array
arr = np.array(100)
print(arr)

# Create a NumPy 1-D array
Myarray = np.array([1, 2, 3, 4, 5])
print(Myarray)

# Create a NumPy multidimensional array
Myarr = np.array([[1, 2, 3], [4, 5, 6]])
print(Myarr)
Myarr.ndim

z = np.ones(5, dtype=int)
print(z)

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate([x, y], axis=1))