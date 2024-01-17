def adivinhar_numero_iterativo(numero_secreto):
    menor = 1
    maior = 50
    tentativas = 0

    while menor <= maior:
        meio = (menor + maior) // 2
        tentativas += 1

        resposta = input(f"É o número {meio}? (menor-maior-correto): ")

        if resposta == "correto":
            return tentativas
        elif resposta == "menor":
            maior = meio - 1
        else:
            menor = meio + 1

    return -1

numero_secreto = 33 
resultado = adivinhar_numero_iterativo(numero_secreto)
print(f"Encontrado em {resultado} tentativas!")

