# 1) (3,5 Pontos) Aprendemos que em Python é usual representar uma matriz como uma
# lista de listas. Crie uma função de receba uma matriz representada dessa forma e:
# a) Verifique se ela é uma matriz válida retangular ou quadrada;
# b) Retorne um texto indicando se é válida e qual é o maior valor na matriz;
# c) Se a matriz for quadrada (o número de linhas igual ao número de colunas),
# acrescente ao texto o somatório dos valores da diagonal principal.

# Parâmetro                              Retorno
# M = [[1, 2], [2,3,4], [5, 6]]          Esta não é uma matriz válida
# M = [[1, 2], [2,3], [5, 6]]            Matriz Válida. 2 é o valor mais frequente
# M = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]  Matriz Válida. 3 é o valor mais frequente. Soma da diagonal é 12


def valida_matriz(M):
    rows = len(M)  # linhas
    cols = len(M[0])  # colunas
    maxv = M[0][0]  # maior valor sendo o primeiro
    sumd = 0  # soma das diagonais iniciada em zero
    for r in range(rows):  # para cada linha
        lenr = len(M[r])  # salva o numero de colunas da linha
        if lenr != cols:  # se for diferente de alguma, é inválida
            return "Esta não é uma matriz válida."
        for c in range(cols):  # para cada coluna da linha
            val = M[r][c]  # pega o valor naquela linha e coluna
            if r == c:  # se os índices forem iguais está na diagonal
                sumd += val  # soma a diagonal
            if val > maxv:  # se for maior que o valor máximo
                maxv = val  # atribui o novo valor máximo
    if rows == cols:  # confere se é matriz quadrada
        return f"Matriz válida. O maior número é o {maxv}. O somatório da diagonal principal é {sumd}."
    return f"Matriz válida. O maior número é o {maxv}."


print(valida_matriz([[1, 2], [2, 3, 4], [5, 6]]))
print(valida_matriz([[1, 2], [2, 3], [5, 6]]))
print(valida_matriz([[1, 2, 3], [3, 4, 5], [5, 6, 7]]))
