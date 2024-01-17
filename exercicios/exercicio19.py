salario_atual = float(input("Digite o salário: "))
tempo_servico = int(input("Digite o tempo de serviço: "))

# REAJUSTE
if salario_atual < 500:
    reajuste = 0.25

elif salario_atual <= 1000:
    reajuste = 0.20

elif salario_atual <= 1500:
    reajuste = 0.15

elif salario_atual <= 2000:
    reajuste = 0.10
    
else:
    reajuste = 0
# BONUS
if tempo_servico < 1:
    bonus = 0

elif tempo_servico >= 1 and tempo_servico <= 3:
    bonus = 100
    
elif tempo_servico >= 4 and tempo_servico <= 6:
    bonus = 200
    
elif tempo_servico >= 7 and tempo_servico <= 10:
    bonus = 300

else:
    bonus = 500

aumento = salario_atual * reajuste
novo_salario = salario_atual + aumento + bonus

print("O novo salário do funcionário é R$ {:.2f}".format(novo_salario))