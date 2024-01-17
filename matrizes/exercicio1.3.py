matriz = [['Pedro',22],['Ana',15],['Paula',12]]

pessoa = ['Jean', 41]
matriz.insert(3, pessoa)
matriz.pop(1)

print('--'*16)
print('MATRIZ')
print('--'*16)
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|', end='\t')
        print(matriz[lin][col], end='\t')
    print('|')
    print('--'*16)
        