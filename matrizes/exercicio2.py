matriz = [['Pedro',22],['Ana',15],['Paula',12]]

print('--'*16)
print('MATRIZ')
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|', end='\t')
        print(matriz[lin][col], end='\t')
    print('|')
    print('--'*17)
        
print('O elemento que consta na linha 0 e coluna 0 é', matriz[0][0])
print('O elemento que consta na linha 1 e coluna 0 é', matriz[1][0])