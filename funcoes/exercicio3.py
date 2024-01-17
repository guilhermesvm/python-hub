valor = int(input('Digite um valor para saber sua natureza: '))

def positivo_negativo_zero(valor):
    if valor > 0:
        return print('O número é positivo.')
    elif valor < 0:
        return print('O número é negativo.')
    else:
        print('O número é zero.')
positivo_negativo_zero(valor)