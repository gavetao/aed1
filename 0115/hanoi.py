# torre de hanói 3 discos


def hanoi(numDiscos, origem, destino, auxiliar):
    if numDiscos == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    hanoi(numDiscos - 1, origem, auxiliar, destino)
    print(f"Mova o disco {numDiscos } de {origem} para {destino}")
    hanoi(numDiscos - 1, auxiliar, destino, origem)
