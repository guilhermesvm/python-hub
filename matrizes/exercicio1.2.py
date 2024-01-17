matriz = [['Pedro',22],['Ana',15],['Paula',12]]

pessoa = ['Jean', 41]
matriz.insert(3, pessoa)

print('--'*16)
print('MATRIZ')
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|', end='\t')
        print(matriz[lin][col], end='\t')
    print('|')
    print('--'*16)
        
