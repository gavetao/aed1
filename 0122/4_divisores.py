# 4) Faça uma função em Python que receba, por parâmetro, um número inteiro x > 0, e
# retorne o número de divisores positivos que x tem. Por exemplo: o número 12 tem 6
# divisores (1, 2, 3, 4, 6 e 12).


def divisores(n):
    return [d for d in range(1, n + 1) if n % d == 0]
