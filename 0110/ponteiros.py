# ponteiros sao variaveis que apontam para determinado espaço de memória

import sys
texto = ['678']
print('ponteiros --> ',sys.getrefcount(texto)) # vai dar 2,  sys + texto
outro = texto
print(texto,id(texto))
print(outro,id(outro))
print('-------------')
print('pointeiros --> ',sys.getrefcount(texto)) # vai dar 3, sys + texto + outro


def incrementaInt(x) : # como numero é uma variavel imutavel, ele cria novo slot para função
    print(x,id(x)) # global
    x +=1
    print(x,id(x)) # global

x = 15
print(x,id(x)) # local
incrementaInt(x)
print(x,id(x)) # global

def incrementaLista(y) : # como lista é uma variavel mutável, usa o mesmo slot de memória, as funções criam variaveis novas, mas apontam para o mesmo slot
    print(y,id(y)) # global
    y[0] += 1
    print(y,id(y)) # global

y = [15]
print(y,id(y)) # global
incrementaLista(y)
print(y,id(y)) # global
