import numpy as np
print('-=-=-=-=-=-=-=-=-=-=-=-=-=MATRIZES A-=-=-=-=-=-=-=-=-=-=-=-=-= ')
a = np.array([[1,2,3,4,5,6,7,],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,32,33,34,35]])
print(a)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=MATRIZE B-=-=-=-=-=-=-=-=-=-=-=-=-= ')
b = np.array([[32,12,33,43,55,46,17,],[28,95,1,11,212,88,23],[78,76,54,64,29,4,6],[81,21,3,99,44,8,7],[56,20,61,69,15,36,38]])
print(a)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ')

soma_a = a.sum()
print("Soma da matriz A é {}".format(soma_a))
print('-=' * 30)
soma_b = b.sum()
print("Soma da matriz B é {}".format(soma_b))
print('-=' * 30)
total = soma_a + soma_b
print("Total somando entre as matrizes é {}".format(total))
