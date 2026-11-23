def ler_texto():
    linhas = []

    while True:
        linha = input()
        if linha.strip().upper() == 'FIM':
            break
        else:
            linhas.append(linha)
    return "\n".join (linhas)

def analisar_texto(texto):
    if texto.strip() == "":
        print("O texto está vazio.")
        return False
    elif texto.strip().isdigit():
        print("opa, não dá para resumir números!")
        return False
    else:
        print("Texto recebido!")
        return True