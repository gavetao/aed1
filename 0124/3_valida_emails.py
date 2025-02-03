# 3) (3,5 Pontos) Um email válido possui o seguinte formato:
# nome_do_utilizador@subdominio.dominio
# O arquivo emails.txt possui uma lista de emails. No entanto, alguns emails não
# foram digitados corretamente e precisam ser corrigidos. Leia o arquivo email.txt e
# crie um novo arquivos emails_invalidos.txt apenas com os emails inválidos.

# Veja alguns exemplos:

# # E-mails válidos
# joao.silva@gmail.com
# maria_oliveira@outlook.com
# ana123@yahoo.com.br
# contato@empresa.com
# jose-da-silva@provedor.net
# email.teste@sub.dominio.com
# andre.prisco@furg.br

# # E-mails inválidos
# joao.silva_gmail.com  # Falta o "@"
# @outlook.com          # Falta o nome antes do "@"
# maria@@yahoo.com.br   # Dois "@"
# anateste@.com         # Servidor ausente
# email@dominio..com    # Dois pontos consecutivos
# ana@dominio,com       # Vírgula ao invés de ponto
# sem-arroba-sem-nada   # Sem "@" e domínio
# 123@456.789           # Domínio apenas numérico


def valida_email(email: str):
    invalidos = [",", ";", ":", "?", "!"]  # lista de caracteres invalidos

    for c in email:  # procura por caracteres ivalidos
        if c in invalidos:
            return False

    # procura o @ no email utilizador@servidor
    if not "@" in email:
        return False

    # divide o email em utilizador@servidor => [utilizador, servidor]
    utilizador, servidor, *rest = email.split("@")

    # se tiver mais de um valor utilizador@servidor@resto => [utilizador, servidor, [resto]]
    if len(rest):
        return False

    # se algum deles for vazio @servidor => ["", servidor] / utilizador@ => [utilizador, ""]
    if not len(utilizador) or not len(servidor):
        return False

    # procura o . no servidor subdominio.dominio
    if not "." in servidor:
        return False

    # dividie o servidor em  subdominio1.subdominio2.dominio => [[subdominio1, subdominio2], dominio]
    *subdominios, dominio = servidor.split(".")

    # se o dominio for vazio subdomionio. => [[subdominio], ""]
    if not len(dominio):
        return False

    # se algum dos subdominios for vazio subdominio1..dominio => [[subdominio, ""], dominio]
    if 0 in [len(s) for s in subdominios]:
        return False

    return True


def valida_emails(emails: list):
    with open("emails_invalidos.txt", "w", encoding="utf-8") as f:
        for email in emails:
            if not valida_email(email):
                f.write(email + "\n")


with open("email.txt", "r", encoding="utf-8") as f:
    emails = [e[:-1] if "\n" in e else e for e in f.readlines()]
    # le cada linha do documento de emails e extrai o "\n" se existir

valida_emails(emails)
