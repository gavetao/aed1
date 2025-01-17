# muda endereço de memória
texto = "oi"
print(texto, id(texto))
texto += "tchau"
print(texto, id(texto))

# muda endereço de memória
texto = "oi"
outro = texto
print(texto, id(texto))
print(outro, id(outro))
print("--------------")
texto += "tchau"
print(texto, id(texto))
print(outro, id(outro))

# nao muda endereço de memória
texto = ["A", "B", "C"]
print(texto, id(texto))
texto[0] = "X"
print(texto, id(texto))
