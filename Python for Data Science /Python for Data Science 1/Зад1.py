import numpy as np

file_path = r'C:\Users\Egor\Desktop\Питон\Задания\Python\Python\Часть2\Python for Data Science 1\Mat.txt'

matrix = np.genfromtxt(file_path, delimiter=',')

print(matrix)


max_value = np.amax(matrix)
min_value = np.amin(matrix)
max_index = np.unravel_index(np.argmax(matrix, axis=None), matrix.shape)
min_index = np.unravel_index(np.argmin(matrix, axis=None), matrix.shape)
matrix[max_index], matrix[min_index] = min_value, max_value

print(matrix)
