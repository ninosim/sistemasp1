# Usando um arquivo de funções separado, desenvolva um sistema que receba um produto, seu peso e o seu valor em dólar.
# Faça a conversão para reais (considerar o dólar R$5,09) e, calcule o valor do seu frete (considerar 100g = $1,99).
# Informe o valor do produto convertido para real
# Informe o valor do frete convertido para real
# Informe o valor total da compra, convertido para real

from funcoes import compra_dolar

produto = str(input("Digite o nome do produto: "))

# O nome do produto está por fora pq idealmente uma função não deve receber parâmetros que não serão utilizados dentro dela.

peso = float(input("Digite o peso do produto (em gramas): "))
valor_dolar = float(input("Digite o valor do produto (em dólares): $ "))

lista = compra_dolar(peso, valor_dolar)

print(f"O valor do produto {produto} em reais é R$ {lista[0]:.2f}, o valor do seu frete é R$ {lista[0]:.2f}. O valor total de sua compra é R$ {lista[1]:.2f}.")