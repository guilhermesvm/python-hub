idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você pode fazer a carteira de motorista AB.")
    if idade >= 21:
        print("Você também pode fazer a carteira de motorista D.")
else:
    print("Você ainda não tem idade suficiente para fazer a carteira de motorista.")
