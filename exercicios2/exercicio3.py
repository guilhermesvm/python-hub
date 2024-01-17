#Desenvolva um jogo de perguntas, onde um jogador pensa em um número no intervalo de 1 a n.
#O Segundo jogador tenta adivinhar o número fazendo perguntas do tipo: "o número é menor/maior que X?"
#O objetivo do jogo é descobrir o número fazendo menos perguntas possíveis.


print('Jogo de Perguntas!')
print('Vou tentar adivinhar o número que você está pensando no menor número de chances possível.')
vmaximo = int(input('Digite o valor máximo para jogar: '))

def jogo_perguntas():
    menor = 1
    maior = vmaximo
    tentativas = 0
    while menor <= maior:
        meio = (menor + maior) // 2
        tentativas += 1
        resposta = str(input(f"O número é maior, menor ou igual a {meio}? "))
        
        if resposta == "igual":
            print("O número que você pensou é {}!".format(meio))
            return tentativas
            break
        elif resposta == "menor":
            maior = meio - 1
        elif resposta == "maior":
            menor = meio + 1
        else:
            print('Resposta inválida.')
            
        if menor > maior:
            print("Não consegui adivinhar o número que você pensou.")


resultado = jogo_perguntas()
print(f"Encontrado em {resultado} tentativa(s)!")