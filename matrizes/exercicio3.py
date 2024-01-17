print('-----------Preenchendo a Matriz-----------')
num00 = int(input('Digite um número na posição[0],[0]: '))
num01 = int(input('Digite um número na posição[0],[1]: '))
num10 = int(input('Digite um número na posição[1],[0]: '))
num11 = int(input('Digite um número na posição[1],[1]: '))
num20 = int(input('Digite um número na posição[2],[0]: '))
num21 = int(input('Digite um número na posição[2],[1]: '))

matriz = [[num00,num01,num10],[num11,num20,num21]]
print('----------------Imprimindo a Matriz----------------')

for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|', end='\t')
        print(matriz[lin][col], end='\t')
    print('|')
    print('--'*25)
        
