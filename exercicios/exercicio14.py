# 14 – Peça para o usuário digitar um numero, em seguida exibir a mensagem dizendo se o numero é PAR ou IMPAR.

numero = int(input("Digite o primeiro valor: "))

resto = numero % 2 # Aqui a variavel resto é feito o calculo da variavel numero, trazendo o resto da divisão

# Nese IF(se) está comparando o resto da divisão por 0, pois qualquer resto de divisão = 0 o numero e PAR
# ELSE (senão) caso o IF não seja verdadeiro, == 0 , automaticamente vai cair no else.
if (resto == 0):
    print("O numero digitado pelo usuário e PAR")
else:
    print("O numero digitado pelo usuário é IMPAR")