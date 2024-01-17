numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um segundo número: '))

if numero1 == numero2:
    print('Valores iguais não podem ser lidos')
    
else:
    print('Os números dentro desse intervalo são:')
    for lista in range(numero1, numero2):
        print(lista)
    