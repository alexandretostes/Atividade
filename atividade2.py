#Crie um método que receba duas matrizes, some os valores total de cada matriz e depois miltiple o resultado dela e retorne o valor
import random

m1 = [[0,0,0], [0,0,0], [0,0,0]]
m2 = [[0,0,0], [0,0,0], [0,0,0]]

for l in range(0, 3):
    for c in range(0, 3):
       m1[l][c]= random.randint(0,100)
               #float(input(f'Digite um valor para primeira matriz [{l}], [{c}]:'))
for x in range(0, 3):
    for y in range(0, 3):
       m2[x][y] = random.randint(0,100)
                #float(input(f'Digite um valor para segunda matriz [{x}], [{y}]:'))
print('-=' * 30)
print('PRIMEIRA MATRIZ')
for matriz1 in m1:
        print(matriz1)
print('-=' * 30)
print('SEGUNDA MATRIZ')
for matriz2 in m2:
        print(matriz2)
print('-=' * 30)

s1 = 0
s2 = 0
for sm in m1:
        for sm1 in sm:
            s1 = s1 + sm1
print('-=' * 30)
print('A soma da primeira matriz é: ')
print(s1)
print('-=' * 30)

for smz in m2:
        for sm2 in smz:
            s2 = s2 + sm2
print('-=' * 30)
print('A soma da segunda matriz é: ')
print(s2)
print('-=' * 30)
mult = s1 * s2
print('-=' * 30)
print('A multiplicação entre as matrizes é {:.0f}'.format(mult))

