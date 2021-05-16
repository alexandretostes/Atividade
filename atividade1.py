#Você tem uma lista, a ideia do exercicio é tirar a media de todos os valors contidos na lista, porém para fazer
# o calculo precisa remover as strings

lista = [6,7,4,7,8,4,2,5,7,'hum','dois']

lista = [x for x in lista if type(x) != str]
total = sum(lista)
media = total / len(lista)

print('A media é {}'.format(media))