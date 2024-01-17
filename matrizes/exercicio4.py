matriz = [['Ana', 22], ['Julia', 26],['Santa',48]]

print('=='*16)
print('IMPRIMINDO A MATRIZ')

for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|', end='\t')
        print(matriz[lin][col], end='\t')
        print('|')
        print('--'*12)

