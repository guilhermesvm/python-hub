numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
pares = 0
impares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print ('A lista contém', pares, ' números pares e', impares, 'números ímpares.')