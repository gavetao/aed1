# fibonacci sucessao de numeros inteiros que começa com 0 e 1 onde cada número seguinte é a soma dos dois anteriores:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)
