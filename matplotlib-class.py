# import matplotlib.pyplot as plt
# import numpy as np
#
#
# xpoints = np.array([0,6])
# ypoints = np.array([0,250])
# plt.plot(xpoints, ypoints)
# plt.show()

#
# print(plt.plot([1,2,3,4]))
#
# print(plt.show())
#
#
# x = np.arrange(0, 10, 0.1)

# import numpy  as np
# import matplotlib.pyplot as plt
# x=np.arange(0,3*np.pi,0.1)
# print(x)
# y=np.sin(x)
# print(y)
# plt.plot(x,y)
# plt.show()

# plt.figure(figsize=(10,5))
# plt.plot([1,2,3,4])

# import matplotlib.pyplot as plt
# # Sample data: Years and corresponding population
# years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021,
# 2022]
# population = [500000, 550000, 600000, 650000, 700000, 750000,
# 800000, 850000, 900000, 950000]
# # Plotting the line
# plt.scatter(years, population)
# # Adding title and labels
# plt.title('City Population Growth Over 10 Years')
# plt.xlabel('Year')
# plt.ylabel('Population')
# # Display the plot
# plt.grid(True)
# plt.show()
# import numpy as np
# def calculate_stats(random_array):

#  mean_value = np.mean(random_array)
#  median_value = np.median(random_array)
#  std_deviation = np.std(random_array)

#  return mean_value, median_value, std_deviation
# np.random.seed(42)
# random_array = np.random.randint(1, 100, 20)
# mean, median, std_dev = calculate_stats(random_array)
# print("Random Array:", random_array)
# print("Mean:", mean)
# print("Median:", median)
# print("Standard Deviation:", std_dev)

# import numpy as np
# # Define two matrices
# matrix_A = np.array([[1, 2, 3], [4, 5, 6]])
# matrix_B = np.array([[7, 8], [9, 10], [11, 12]])
# # Perform matrix multiplication using the dot product
# result_matrix = np.dot(matrix_A, matrix_B)
# print("Matrix A:")
# print(matrix_A)
# print("\nMatrix B:")
# print(matrix_B)
# print("\nResult of Matrix Multiplication (A * B):")
# print(result_matrix)


import pandas as pd
import seaborn as sns

# Load the iris dataset from seaborn
iris = sns.load_dataset('iris')
# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(iris.head())
# Display basic statistics for a specific column (e.g., 'sepal_length')
column_name = 'sepal_length'
column_statistics = iris[column_name].describe()
print(f"\nBasic statistics for column '{column_name}':")
print(column_statistics)