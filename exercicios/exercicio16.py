# 16 - Crie um algoritmo que verifique o tipo de triângulo, se ele é equilátero, isósceles ou escaleno.

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("O triângulo é EQUILÁTERO.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é ISÓSCELES.")
    else:
        print("O triângulo é ESCALENO.")
else:
    print("Não é possível formar um triângulo.")
