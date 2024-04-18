def compra_dolar(peso, valor_dolar):
    cotacao_dolar = 5.09
    valor_real = valor_dolar * cotacao_dolar
    frete_dolar = (peso / 100) * 1.99
    frete_real = frete_dolar * cotacao_dolar
    return [valor_real, frete_real]

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