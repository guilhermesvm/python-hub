contador = 0
soma = 0

for contagem in range(1, 101):
    if contagem % 2 == 0:
        soma += contagem
        contador += 1
        
print('A soma é: ', soma)
print('Os números PARES, de 1 a 100, são:', contador)
        