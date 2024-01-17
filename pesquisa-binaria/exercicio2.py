def adivinhar_numero_recursiva(numero_secreto, menor, maior, tentativas):
    meio = (menor + maior) // 2
    tentativas += 1

    resposta = input(f"É o número {meio}? (menor-maior-correto): ")

    if resposta == "correto":
        return tentativas
    elif resposta == "menor":
        return adivinhar_numero_recursiva(numero_secreto, menor, meio - 1, tentativas)
    elif resposta == "maior":
        return adivinhar_numero_recursiva(numero_secreto, meio + 1, maior, tentativas)
    else:
        return ('Resposta inválida.')

numero_secreto = 7
resultado = adivinhar_numero_recursiva(numero_secreto, 1, 150, 0)
print(f"Encontrado em {resultado} tentativas!")
