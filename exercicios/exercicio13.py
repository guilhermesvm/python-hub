# 13 – Desenvolva um algoritmo que peça para o usuário dar entrada em dois valores, em seguida faça a soma e verifique se os valores são maior ou igual a 100.

valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))

soma = valor_1 + valor_2

if (soma >= 100):
    print("A soma dos valores é = ",soma, "sendo maior ou igual a 100")
else:
    print("A soma dos valores é menor que 100")