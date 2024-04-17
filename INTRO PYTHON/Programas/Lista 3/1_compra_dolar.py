# Usando um arquivo de funções separado, desenvolva um sistema que receba um produto, seu peso e o seu valor em dólar.
# Faça a conversão para reais (considerar o dólar R$5,09) e, calcule o valor do seu frete (considerar 100g = $1,99).
# Informe o valor do produto convertido para real
# Informe o valor do frete convertido para real
# Informe o valor total da compra, convertido para real

from funcoes import compra_dolar

compra_dolar(str(input("Digite o nome do produto: ")), 
            float(input("Digite o peso do produto (em gramas): ")),
            float(input("Digite o valor do produto (em dólares): $ ")))