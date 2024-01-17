lista = ['Brasil', 'Argentina','Uruguai','Paraguai']

print('Lista Original:', lista)

print('Foram encontrados', len(lista),'elementos na lista original.')

print('Foi encontrado', lista.count('Paraguai'),' ocorrência de "Paraguai" na lista original.')

print('O terceiro elemento encontrado na lista foi:', lista[2])

lista.insert(2,'México')
print('Foi adicionado México no índice 2 da lista original:', lista)

lista.sort()
print('Nova lista ordenada:', lista)

print('O país "França" foi localizado na lista.', 'França' in lista)

lista.remove('Brasil')
print('O pais "Brasil" foi removado da lista.', lista)

lista.reverse()
print('A lista foi invertida:', lista)


