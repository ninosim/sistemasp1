def cumprimento (*nomes): #o asterico permite o envio de qualquer quantidade de parâmetros 
    for nome in nomes:
        print("Oi " + nome + "!")

nomes = input("Qual é o seu nome?")
cumprimento (nomes)