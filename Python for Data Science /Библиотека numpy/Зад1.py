import numpy as np
data = np.genfromtxt(r'C:\Users\Egor\Desktop\Питон\Задания\Python\Python\Часть2\Библиотека numpy\mat.txt', delimiter=',')
identity_matrix = np.genfromtxt(r'C:\Users\Egor\Desktop\Питон\Задания\Python\Python\Часть2\Библиотека numpy\ed.txt', delimiter=',')

result = np.dot(data, identity_matrix)
print (result)
np.savetxt(r'C:\Users\Egor\Desktop\Питон\Задания\Python\Python\Часть2\Библиотека numpy\output.txt', result, fmt='%d', delimiter=',') 