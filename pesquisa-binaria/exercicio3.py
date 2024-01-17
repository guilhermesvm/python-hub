def pesquisa_binaria(lista, posicao, inicio, fim):
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == posicao:
            return meio
        elif lista[meio] < posicao:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

lista = [1, 3, 5, 7, 9]
posicao = 5
resultado = pesquisa_binaria(lista, posicao, 0, len(lista) - 1)

if resultado != -1:
    print("O elemento está presente no índice " + str(resultado))
else:
    print("Não encontrado.")
    
    