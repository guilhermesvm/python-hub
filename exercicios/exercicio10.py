#11 – Desenvolva um algoritmo que peça para o
# usuário dar entrada em dois valores, em seguida verifique
# se o primeiro valor é maior que o segundo.

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

if nota_1 < nota_2:
    print("A primeira nota = ",nota_1, "é maior que a segunda = ",nota_2)
else:
    print("O valor da segunda nota e maior que a primeira")