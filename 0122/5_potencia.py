# 5) Faça uma função em Python para calcular X elevado à Y, ou X^Y. A função deverá receber,
# por parâmetro, X e Y, e retornar o resultado da chamada da subrotina. Exemplo: 2 elevado à
# 3 é igual à 2*2*2 = 8. Os parâmetros são 2 e 3, e o retorno será 8. Obs: implementar
# exatamente como no exemplo, ou seja, a exponenciação deve ser calculada por
# multiplicações sucessivas.


def potencia(x, y):
    p = x
    for _ in range(y - 1):
        p *= x
    return p
