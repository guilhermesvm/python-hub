from random import randint
computador = randint(1, 10)


for i in range(3):
    if i == 0:
        jogada = int(input('PRIMEIRA JOGADA! Digite um número de 1 a 10: '))
        
    elif i == 1:
        jogada = int(input('SEGUNDA JOGADA! Digite um número de 1 a 10: '))
    
    elif i == 2:
        jogada = int(input('TERCEIRA JOGADA! Digite um número de 1 a 10: '))
        
    if jogada > 10:
        print('Jogada inválida!')
        break
    
    print('Você jogou {}'.format(jogada))
    print('Computador jogou {}'.format(computador))
    if jogada == computador:
        print('Você acertou o número!')
        break
    else:
        print('Você errou.')
        print('--'*19)
    