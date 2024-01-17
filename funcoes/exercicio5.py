"""Desenvolva uma função que solicite ao usuário uma lista de 8 números.
Verifique quais números de 0 á 25 estão presentes na lista.
Mostre a quantidade de números retornados e quais foram"""

# Define a função.
def verificar_numeros():
    # Crirar lista vazia, onde é armazenado as notas das avaliações
    lista = []
    print("Digite 8 números:")
    
    # Laço de repetição utilizado para interagir 8 vezes.
    for i in range(8):
        numero = int(input("Número {}: ".format(i+1)))
        
        # Adiciona os numeros a lista que estava vazia, usando o append para inserir cada numero nova no final dela.
        lista.append(numero)
    
    # Criado 2 conjuntos construidos apartir da lista.
    # Set é usado apra criar esses conjuntos, sendo uma coleção de elementos unicos.
    numeros_presentes = set(lista)
    numeros_desejados = set(range(26))
    
    # Interseção é um metodo usado para verificar e identificar quais numeros digitados pelo usuário estão dentro do conjunto de numeros digitados
    # Ou seja quais numeros estão na interseção entre esses conjuntos (numeros_presentes, numeros_desejados)
    
    numeros_encontrados = numeros_presentes.intersection(numeros_desejados)
    quantidade_encontrada = len(numeros_encontrados)

    print("Quantidade de números encontrados:", quantidade_encontrada)
    print("Números encontrados:", numeros_encontrados)
    
# Chamada da função, usada para iniciar a execução do bloco de códigos
verificar_numeros()
