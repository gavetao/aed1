# fatorial fórmula: n! = n*(n-1)! com 0! = 1


def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)
