# Calcular o indice de massa corporal

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (metros): "))
imc = peso / altura**2
print("Seu IMC é:", imc)
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Seu peso está normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
elif imc < 35:
    print("Você está com obesidade grau 1.")
elif imc < 40:
    print("Você está com obesidade grau 2.")
else:
    print("Você está com obesidade grau 3 (mórbida).")
