from random import randint
jogadas = ('Pedra','Papel','Tesoura')
computador = randint (0, 2)

print('-------JOKENPÔ!-------')
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))
print('--'*16)
print('Computador jogou {}'.format(jogadas[computador]))
print('Jogador jogou {}'.format(jogadas[jogador]))
print('--'*16)

if computador == 0: #computador joga PEDRA #
    if jogador == 0:
        print('Empate.')
    elif jogador == 1:
        print('Jogador vence!')
    elif jogador == 2:
        print('Computador vence!')
    else:
        print('Jogada inválida!')

if computador == 1: #computador joga PAPEL
    if jogador == 0:
        print('Computador vence!')
    elif jogador == 1:
        print('Empate.')
    elif jogador == 2:
        print('Jogador vence!')
    else:
        print('Jogada inválida!')

if computador == 2: #computador joga TESOURA
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2:
        print('Empate.')
    else:
        print('Jogada inválida!')
        