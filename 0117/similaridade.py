# 1) Similaridade de strings
# Crie uma função que receba 2 strings e retorne a similiaridade entre elas.


def distance(a: str, b: str, d: int = 0):
    if not len(a):
        return d + len(b)
    if a[0] in b:
        i = b.index(a[0])
        return distance(a[1:], b[0:i] + b[i + 1 :], d)
    d = d + 1
    return distance(a[1:], b[1:], d)
