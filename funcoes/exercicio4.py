def media_final():
    disciplina = str(input('Digite o nome da disciplina: '))

    nota1 = int(input('Digite a nota da avaliação 1: '))
    nota2 = int(input('Digite a nota da avaliação 2: '))
    nota3 = int(input('Digite a nota da avaliação 3: '))
    nota4 = int(input('Digite a nota da avaliação 4: '))

    soma_notas = nota1 + nota2 + nota3 + nota4
    media = soma_notas / 4
    media_minima = 7.0
    print('A disciplina é:', disciplina)
    print('A sua média foi', media)
    
    if media >= media_minima :
        return print('Parabéns! Você passou.')
    else:
        return print('Reprovado.')
    
media_final()