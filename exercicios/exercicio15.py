# 15 – Desenvolva um algoritmo que peça para o usuário dar entrada em dois valores, em seguida exiba o resultado da:
# Soma - Subtracao - Multiplicacao - Divisao

# Multiplique a subtração com a divisão

# Verifique se o resultado é menor que a multiplicação.

# Caso seja menor, faça a soma do resultado com a primeira valor



valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))

soma = valor_1 + valor_2
subtracao = valor_1 - valor_2
multiplicacao = valor_1 * valor_2
divisao = valor_1 / valor_2

# Multiplique a subtração com a divisão
resultado = subtracao * divisao

print ("Valor total da soma = ",soma)
print ("Valor total da subtracao = ",subtracao)
print ("Valor total da multiplicacao = ",multiplicacao)
print ("Valor total da divisao = ",divisao)

#Verifique se o resultado é menor que a multiplicação.
if (resultado < multiplicacao):
# Caso seja menor, faça a soma do resultado com a primeira valor
    print(resultado + valor_1)
    
    