lista = ['Starchild','Demon','Spaceman','Cat','Fox','Ankh Warrior']
lista2 = ['Bandit', 'Hawk']
listaConcatenada = lista + lista2

listaNumeros = [0, 1, 1.5, 2, 3, 4]

print(lista) #Visualizar a primeira lista
print('--'*16)
print(lista[2]) #Visualizar o 2º índice da lista
print('--'*16)
print(lista[0:4]) #Visualizar o intervalo de 0 a 4
print('--'*16)
print(listaConcatenada) #Junta duas listas
print('--'*16)
print('Spaceman' in lista) #Verifica se o elemento está presente na lista
print('--'*16)
print(min(listaNumeros)) #Apresenta o menor número da lista
print(max(listaNumeros)) #Apresenta o maior número da lista
print(sum(listaNumeros)) #Apresenta a soma dos números da lista
print('--'*16)
print(len(lista)) #Apresenta a quantidade de elementos presentes da na lista
print('--'*16)
print(lista.count('Spaceman')) #Apresenta o número de vezes que o elemento está na lista
print('--'*16)
lista.insert(6,'Bandit') #Adiciona o elemento no índice escolhido
print(lista)
print('--'*16)
lista.remove('Bandit') #Remove o elemento da lista
print(lista)
print('--'*16)
lista.pop()
print(lista) #Remove o último item. É possível escolher qual item será removido adicionando o índice correspondente no ()
print('--'*16)
lista.sort() #Reorganiza os items por ordem alfabética
print(lista)
print('--'*16)
lista.reverse() #Inverte a posição dos itens na lista
print(lista)
print('--'*16)
lista.append('GUILHERME') #Adiciona um elemento no final da ista
print(lista)
print('--'*16)
lista.clear() #Remove todos os itens da lista
print(lista)