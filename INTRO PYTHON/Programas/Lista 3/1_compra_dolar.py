# Usando um arquivo de funções separado, desenvolva um sistema que receba um produto, seu peso e o seu valor em dólar.
# Faça a conversão para reais (considerar o dólar R$5,09) e, calcule o valor do seu frete (considerar 100g = $1,99).
# Informe o valor do produto convertido para real
# Informe o valor do frete convertido para real
# Informe o valor total da compra, convertido para real

def compra_dolar():
    produto = input("Digite o nome do produto: ")
    peso = float(input("Digite o peso do produto (em gramas): "))
    valor_dolar = float(input("Digite o valor do produto (em dólares): $ "))
    cotacao_dolar = 5.09
    valor_real = (valor_dolar * cotacao_dolar)
    frete_dolar = (peso / 100) * 1.99
    frete_real = frete_dolar * cotacao_dolar
    print(f"O valor do produto {produto} em reais é R$ {round(valor_real, 2)}, o valor do seu frete é de R$ {round(frete_real, 2)}. O valor total de sua compra é de R$ {round((valor_real + frete_real), 2)}.")

compra_dolar()