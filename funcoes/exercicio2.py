def achar_maior_valor():
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))

    if valor1 > valor2:
        return print('O maior valor é:',valor1)  
    elif valor2 > valor1:
        return print('O maior valor é:',valor2)
    else:
        return print('Os valores são iguais.')
    
achar_maior_valor()
        