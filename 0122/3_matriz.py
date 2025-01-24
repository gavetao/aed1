# 3) Faça um programa em Python que crie uma matriz de inteiros de cinco linhas por dez
# colunas. Leia os valores desta matriz linha após linha, e exiba a matriz na tela coluna por
# coluna.

matrix = [[int(input(f"matrix[{j}][{i}]: ")) for i in range(10)] for j in range(5)]

for i in range(10):
    for j in range(5):
        print(matrix[j][i])
