contador = 0

for i in range(4):
    n1=float(input('Digite a nota 1: '))
    n2=float(input('Digite a nota 2: '))
    media= (n1+n2)/2
    print('Média do aluno: ', media)
    if media < 5.0:
        contador = contador + 1
        
print('A quantidade de alunos reprovados é:', contador)