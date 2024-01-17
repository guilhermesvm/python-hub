#Desenvolva um jogo de perguntas, onde um jogador pensa em um país da américa do sul.
#O computador vai tentar adivinhar o país fazendo perguntas do tipo: “antes, igual ou depois“, seguindo a ordem alfabética.
#O objetivo do jogo é descobrir o país fazendo menos perguntaspossíveis

def jogo_adivinhacao_pais():
    paises = [
        "Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador",
        "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"]
    inicio = 0
    fim = len(paises)
    print('Pense em um pais da América do Sul.')
    print('Vou tentar adivinhar o pais que você está pensando no menor número de chances possível.')
    while inicio <= fim:
        meio = (inicio+fim) // 2

        resposta = input("O pais que você pensou é antes, depois ou igual a {}? ".format(paises[meio]))
        
        if resposta == "igual":
            return print("O país que você pensou é {}!".format(paises[meio]))
            break
        elif resposta == "antes":
            fim = meio - 1
        elif resposta == "depois":
            inicio = meio - 1
        else:
            print("Desculpe, não entendi sua resposta. Por favor, responda 'antes', 'igual' ou 'depois'.")
            
        if inicio > fim:
            print("Não consegui adivinhar o país que você pensou.")
       
jogo_adivinhacao_pais()     
        
        
