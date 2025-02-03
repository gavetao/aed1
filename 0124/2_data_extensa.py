# 2) (3,0 Pontos) Crie uma função que receba uma data em formato DD/MM/AAAA e
# retorne seu nome por extenso. A função deve receber como parâmetro o nome da
# cidade base. Considere que a data entregue é válida. Não precisa perder tempo
# validando a data.

# Parâmetro                   Retorno
# "24/01/2025", "Rio Grande"  "Rio Grande, 24 de janeiro de 2025."
# "01/04/4000", "Marte"       "Marte, 1º de abril de 4000."
# "31/5/2000", "Itu"          "Itu, 31 de maio de 2000."


def data_extensa(data: str, lugar: str):
    meses = [
        "janeiro",
        "fevereiro",
        "março",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro",
    ]  # lista com os meses do ano
    dia, mes, ano = [int(x) for x in data.split("/")]  # separa a data em dia mes e ano
    # retorna o lugar, o dia (1º se dia == 1), o mes baseado no índice da lista e o ano
    return f"{lugar}, {'1º' if dia == 1 else dia} de {meses[mes - 1]} de {ano}."


print(data_extensa("24/01/2025", "Rio Grande"))
print(data_extensa("01/04/4000", "Marte"))
print(data_extensa("31/5/2000", "Itu"))
