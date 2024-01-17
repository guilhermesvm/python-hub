#Desenvolva uma função que solicite ao usuário uma lista de 12 números inteiros de 0 a 100.
#Verifique quais números de 0 á 45 estão presentes na lista. 
#Mostre a quantidade de números retornados e quais foram.
#Crie validações caso o usuário digite informações invalidas ou valores repetidos.


def verificar_numeros():
    lista = []
    print('Digite 12 números inteiros de 0 a 100:')
    for i in range(12):
        numero = int(input("Número {}: ".format(i+1)))
        if numero < 0 or numero > 100:
            print('Número inválido. Digite um número de 0 à 100.')
            continue
        if numero in lista:
            print('Número repetido. Digite outro!')
        lista.append(numero)
        
    numeros_presentes = set(lista)
    numeros_desejados = set(range(46))
    numeros_encontrados = numeros_presentes.intersection(numeros_desejados)
    quantidade_encontrada = len(numeros_encontrados)
    
    print('Quantidade de números encontrados:', quantidade_encontrada)
    print('Números de 1 a 45 encontrados:', numeros_encontrados)
verificar_numeros()
        