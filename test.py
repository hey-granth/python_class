# with open("test.txt", "w") as f:
#     f.write("Hello World\nGranth Agarwal\n")
#
# with open("test.txt", "r") as f:
#     words = f.read().split()
#     print(words)
#     print(len(words))   # all the words
#     f.seek(0)
#     lines = f.readlines()
#     print(lines)
#     print(len(lines))   # all the lines
#     characters = 0
#     for i in words:
#         print(i, end=',')
#         characters += len(i)
#     print(characters)   # all the characters

# # Write to the file
# with open("test.txt", "w") as f:
#     f.write("Hello World\nGranth Agarwal\n")
#
# # Read from the file
# with open("test.txt", "r") as f:
#     # Get all lines in a list
#     lines = f.readlines()
#
#     # Get words by joining lines and splitting
#     words = ' '.join(lines).split()
#
#     print("Words:", words)
#     print("Word count:", len(words))
#     print("Lines:", lines)
#     print("Line count:", len(lines))
#
#     # Calculate characters (excluding spaces)
#     characters = sum(len(word) for word in words)
#     print("Character count (excluding spaces):", characters)

# import matplotlib.pyplot as plt
# # Sample data: Years and corresponding population
# years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021,
# 2022]
# population = [500000, 550000, 600000, 650000, 700000, 750000,
# 800000, 850000, 900000, 950000]
# # Plotting the line
# plt.plot(years, population, marker='o', linestyle='-')
# # Adding title and labels
# plt.title('City Population Growth Over 10 Years')
# plt.xlabel('Year')
# plt.ylabel('Population')
#
# # Display the plot
# plt.grid(True)
# plt.show()

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

import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple GUI")

# Add a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Add a button widget
button = tk.Button(root, text="Click Me", command=lambda: print("Button Clicked"))
button.pack()

# Run the main event loop
root.mainloop()