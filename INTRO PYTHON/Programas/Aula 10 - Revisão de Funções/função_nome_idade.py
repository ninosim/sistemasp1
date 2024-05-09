def cumprimento (nome, idade): #o asterico permite o envio de qualquer quantidade de parâmetros 
    print("Oi " + nome + "!" + " Você tem " + idade + " anos.")

for i in range(10):
    nome = str(input("Qual é o seu nome? "))
    idade = str(input("Qual é a sua idade? "))
    cumprimento (nome, idade)