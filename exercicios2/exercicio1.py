#Desenvolva um jogo, usando pesquisa sequencial, onde o jogador precisa adivinhar um número entre 1 e 100.
#O jogo precisa fornecer dicas para ajudar o jogador a encontrar onúmero correto.
#Mostre o número de tentativas até conseguir acertar o valor.

import random

def facil():
    print('Você tem 20 tentativas.')
    print('Estou pensando em um número de 1 a 100. \n')
    pc = random.randint (1,100)
    tentativas = 0
    while tentativas < 10:
        jogador = int(input('Digite seu palpite: '))
        if pc == jogador:
            print('Você acertou o número!')
            break
        elif  pc >  jogador:
            print('O número que estou pensando é maior.')
        elif pc < jogador:
            print('O número que estu pensando é menor.')
        tentativas += 1
        print("Tentativas:", tentativas, "de 20.")

def medio():
    print('Você tem 10 tentativas.')
    print('Estou pensando em um número de 1 a 100.')
    pc = random.randint (1,100)
    tentativas = 0
    while tentativas < 10:
        jogador = int(input('Digite seu palpite: '))
        if pc == jogador:
            print('Você acertou o número!')
            break
        elif  pc >  jogador:
            print('O número que estou pensando é maior.')
        elif pc < jogador:
            print('O número que estu pensando é menor.')
        tentativas += 1
        print("Suas tentativas estão em ", tentativas, "de 10.")
    print("Computador escolheu ", pc)

def dificil():
    print('Você tem 5 tentativas.')
    print('Estou pensando em um número de 1 a 100.')
    pc = random.randint (1,100)
    tentativas = 0
    while tentativas < 5:
        jogador = int(input('Digite seu palpite: '))
        if pc == jogador:
            print('Você acertou o número!')
            break
        elif  pc >  jogador:
            print('O número que estou pensando é maior.')
        elif pc < jogador:
            print('O número que estu pensando é menor.')
        tentativas += 1
        print("Suas tentativas estão em ", tentativas, "de 5.")
    print("Computador escolheu ", pc)

print('Jogo de Adivinhar!')
print('''
Escolha um nível de dificuldade:
1 - Fácil
2 - Médio
3 - Difícil''')

nivel = int(input('Escolha o nível: '))
if nivel == 1:
    facil()
elif nivel == 2:
    medio()
elif nivel == 3:
    dificil()
else:
    print("Nível inválido.")