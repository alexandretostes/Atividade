import numpy as np
print('-=-=-=-=-=-=-=-=-=-=-=-=-=CRIANDO A MATRIZ-=-=-=-=-=-=-=-=-=-=-=-=-= ')
a = np.array([[1,2,3,4,5,6,7,],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,32,33,34,35]])

print(a)


print('-=-=-=-=-=-=-=-=-=-=-=-=-=TRANSPONDO A MATRIZ-=-=-=-=-=-=-=-=-=-=-=-=-= ')
t = np.transpose(a)
print(t)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=SOMANDO A MATRIZ-=-=-=-=-=-=-=-=-=-=-=-=-= ')

s = a.sum()
print(s)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=SOMANDO TODAS AS COLUNAS MATRIZ-=-=-=-=-=-=-=-=-=-=-=-=-= ')

sc = a.sum(axis=0)
print(sc)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=SOMANDO TODAS AS LINHAS MATRIZ-=-=-=-=-=-=-=-=-=-=-=-=-= ')

sl = a.sum(axis=1)
print("O valor de todas as linhas somas é {}" .format(sl))

print('-=-=-=-=-=-=-=-=-=-=-=-=-=RETORNAR O MAIOR VALOR DA MATRIZ-=-=-=-=-=-=-=-=-=-=-=-=-= ')

mv = a.max()
print("O maior valor da matriz é {}".format(mv))

print('-=-=-=-=-=-=-=-=-=-=-=-=-=RETORNAR O MENOR VALOR DA MATRIZ-=-=-=-=-=-=-=-=-=-=-=-=-= ')

mnv = a.min()
print(mnv)