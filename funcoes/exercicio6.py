def verificar_par_impar(valor):
    valor = int(input('Digite um número para verificar se é par ou ímpar: '))
    if valor % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
print(verificar_par_impar(valor))