#Criar um algoritmo em Python que adicione um menu de opções, conforme apresentado abaixo: (use funções)
#1. Definir o tamanho de uma lista de cidades; 
#2. Inserir as cidades na lista, conforme o tamanho da lista; 
#3. Pesquisa e retorna se existe a ocorrência de uma cidade na lista; 
#4. Exclui uma cidade da lista; 
#5. Exibir os elementos(cidades) da lista; 
#6. Finalizar.
#Crie validações caso o usuário digite informações invalidas ou valores repetidos


def tamanho_lista():
    tamanho = int(input('Informe o tamanho da lista: '))
    print('Tamanho escolhido: ', tamanho)

def inserir_cidades_lista(lista, tamanho):
    for i in range(tamanho):
        nome = str(input(f"Informe a cidade {i+1}: "))
        if nome not in lista_cidades:
            lista_cidades.append(nome)
            print(lista_cidades)
        else:
            print('Cidade já inserida.')
            
def pesquisa_cidade(lista):
    pesquisa = str(input('Digite a cidade que quer pesquisar: '))
    if pesquisa in lista_cidades:
        print(f"A cidade '{pesquisa}' foi encontrada na lista.")
    else:
        print(f"A cidade '{pesquisa}' não foi encontrada na lista.")
        
def deletar_cidade(lista):
    del_nome = str('Digite uma cidade já existente para deletar: ')
    if del_nome not in lista_cidades:
        print('Impossível excluir. Essa cidade não foi inserida previamente.')
    else:
        lista_cidades.remove(del_nome)
        print(f"A cidade '{del_nome} foi removida da lista.")
        print(lista_cidades)
        
def exibir_cidades(lista):
    print('Cidades da lista:')
    print(lista_cidades)
    
            
def menu_opcoes():
    lista_cidades = []
    menu = 0
    
    while menu != 6:
        print('--------------------------------')
        print('MENU DE OPÇÕES')
        print('1 - Tamanho da lista')
        print('2 - Inserir cidade')
        print('3 - Pesquisar cidade')
        print('4 - Excluir cidade da lista')
        print('5 - Exibir cidades da lista')
        print('6 - Sair')
        print('--------------------------')
    
        opcao = int(input('Informe a opção que deseja selecionar: '))
        if opcao == 1:
            lista_cidades.clear()
            tamanho = tamanho_lista()
            print(f"Lista de cidades definida com tamanho {tamanho}")
            
        elif opcao == 2:
            if tamanho == 0:
                print('Defina o tamanho da lista primeiro.')
            else:
                inserir_cidades_lista(lista_cidades, tamanho)
            
        elif opcao == 3:
            if tamanho == 0:
                print('Defina o tamanho da lista primeiro.')
            else:
                pesquisa_cidade(lista_cidades)
        elif opcao == 4:
            if tamanho == 0:
                print('Defina o tamanho da lista primeiro.')
            else:
                deletar_cidade(lista_cidades)
                
        elif opcao == 5:
            if tamanho == 0:
                print('Defina o tamanho da lista primeiro.')
            else:
                exibir_cidades(lista_cidades)
        elif opcao == 6:
            print('Finalizando o programa.')
            break
        else:
            print('Opção inválida. Digite uma opção válida.')
            
menu_opcoes()
    
        