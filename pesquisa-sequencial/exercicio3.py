def encontrar_produto(lista, produto):
    produto = produto.lower()
    if produto in [item.lower() for item in lista]:
        return f"O '{produto.capitalize()}' está na lista de compras."
    else:
        return f"O '{produto.capitalize()}' não está na lista de compras."

lista_compras = ["Arroz", "Queijo", "Pão", "Café"]
produto = input("Digite o nome do produto que deseja verificar: ")
resultado = encontrar_produto(lista_compras, produto)
print(resultado)