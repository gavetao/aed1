# 1) Faça um programa em Python para ler “n” números inteiros, armazenando-os em uma
# lista (o usuário informará um valor inteiro positivo para “n”). Após, crie duas outras listas a
# partir desta primeira digitada, sendo que uma conterá os números positivos (>= 0), e a outra
# conterá os números negativos. Mostre na tela como ficaram as três listas

ints = []
while True:
    n = input()
    if n == "":
        break
    ints.append(int(n))

neg = []
pos = []

for i in ints:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

print(ints)
print(neg)
print(pos)

# 2) Baseado no programa anterior, remova todas as ocorrências do valor zero na lista dos
# números positivos. Mostre na tela as três listas, informando a quantidade de zeros que
# havia, o total de números remanescentes na lista de positivos e na de negativos.

zeros = 0

while 0 in pos:
    zeros += 1
    pos.remove(0)

print(zeros)
print(len(pos) + len(neg))
print(ints)
print(neg)
print(pos)
