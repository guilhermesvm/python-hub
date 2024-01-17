peso = int(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em m): '))
imc = peso / altura ** 2

def calculo_imc(imc):
    imc = peso / altura ** 2
    return imc


print('Seu MMC é: ', calculo_imc(imc))
    