def extrair_pontuacao(dado):
    partes = dado.split(" - ")
    pontuacao = int(partes[0])
    return pontuacao

lista = ["800 - leonardo", "700 - carlos", "1100 - mariana"]
listaord = sorted(lista, key=extrair_pontuacao, reverse=True)
print(listaord)
