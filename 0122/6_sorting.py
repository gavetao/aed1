# 6) Faça um programa em Python que leia duas listas de números compostas por cinco
# elementos informados de maneira ordenada (números em ordem crescente). Crie uma
# terceira lista também ordenada, sendo a união das duas primeiras listas. Exiba as listas, e a
# soma dos seus elementos contidos.

a = [int(input()) for _ in range(5)]
b = [int(input()) for _ in range(5)]

sorted = []

i, j = 0, 0
while i < 5 and j < 5:
    if a[i] < b[j]:
        sorted.append(a[i])
        i += 1
    else:
        sorted.append(b[j])
        j += 1
sorted.append(*a[i:])
sorted.append(*b[j:])

print(sorted)
