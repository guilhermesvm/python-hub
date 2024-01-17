lista_nomes = []
menu = 0
i = 0

while menu != 6:
    print('--------------------------------')
    print('MENU DE OPÇÕES')
    print('1 - Tamanho da lista')
    print('2 - Inserir nomes')
    print('3 - Pesquisar nome')
    print('4 - Excluir nome da lista')
    print('5 - Exibir lista')
    print('6 - Sair')
    print('--------------------------')

    menu = int(input('Informe a opção que dejesa executar: '))

    if menu == 1:
        tamanho = int(input('Informe o tamanho da lista: '))
        print(tamanho)
    elif menu == 2:
            for i in range(tamanho):
                name = str(input("Informe um nome: "))
                if name not in lista_nomes:
                    lista_nomes.insert(i,name)
                else:
                        print("Nome já existe!")
            print(lista_nomes)
    elif menu == 3:
            pesquisa = str(input('Informe o nome para pesquisa: '))
            print(pesquisa in lista_nomes)
            print(lista_nomes)
    elif menu == 4:
            del_nome = str(input('Informe nome a ser deletado: '))
            if del_nome in lista_nomes:
                lista_nomes.remove(del_nome)
            print(lista_nomes)
    elif menu == 5:
            print(lista_nomes)     
    elif menu == 6:
            break
    print('--------------------------------')