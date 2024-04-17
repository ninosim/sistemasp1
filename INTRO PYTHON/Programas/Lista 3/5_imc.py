# 5o Crie uma função que receba como parâmetros o nome, a idade, peso, altura e sexo do usuário.
# Retorne a quantidade de caracteres que possui o nome do usuário, se o usuário é maior ou menor
# de idade, o IMC do usuário e a composição corporal (Abaixo do peso, peso ideal ou sobrepeso),
# de acordo com os dados abaixo.
# Se IMC < 18,5 - Abaixo do peso;
# Se IMC >= 18,5 e <= 25 - Peso ideal;
# Se IMC > 25 – Sobrepeso

def imc(nome, idade, peso, altura):
    print(f"O nome do usuário {nome} tem {len(nome)} caracteres.")
    if idade <= 17:
        print(f"O usuário tem {idade} anos e é menor de idade.")
    else:
        print(f"O usuário tem {idade} anos e é maior de idade.")
    indice = peso / (altura * altura)
    
    if indice < 18.5:
        composicao = "abaixo do peso"
    elif indice < 25:
        composicao = "com peso ideal"
    else:
        composicao = "com sobrepeso"
    print(f"O usuário tem IMC igual a {round(indice, 2)}, e está {composicao}")

nome = input("Digite o nome do usuário: ")
idade = int(input("Digite a idade do usuário: "))
peso = float(input("Digite o peso do usuário: "))
altura = float(input("Digite a altura do usuário: "))
sexo = input("Digite o sexo do usuário: ")

imc(nome, idade, peso, altura)