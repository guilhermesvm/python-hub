def encontrar_valor(lista, valor):
    if valor in lista:
        print('Valor encontrado:', valor)
    else:
         print('Valor nao encontrado. O valor é: ', valor)

numeros = [9, 32, 7, 55, 15]

resultado = encontrar_valor(numeros, 7)
resultado = encontrar_valor(numeros, 6)
