# Crie um algoritmo que receba 4 notas de um estudante, calcule e mostre a média das notas e a mensagem de aprovado se for superior ou igual a 70% ou a mensagem de reprovado se for inferior a 70%.


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
porcentagem_aprovacao = 0.7

if media >= porcentagem_aprovacao * 10:
    print("Sua média é:", media)
    print("Parabéns, você foi aprovado!")
else:
    print("Sua média é:", media)
    print("Infelizmente, você foi reprovado.")
