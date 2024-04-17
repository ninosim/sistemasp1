# 4o Crie uma função que receba como parâmetro uma letra do alfabeto e retorne o valor decimal respectivo a sua ordem no alfabeto.
# Ex.: Caso o atributo passado seja a letra “H”, o retorno deverá ser o número 8.
# O resultado da função deverá ser passado como atributo para outra função que retornará:
# Caso o valor seja par, retornar os valores pares de 2 ao valor passado
# Caso seja ímpar, retornar os valores ímpares de 1 ao valor passado

def letra(entrada):
    alfabeto = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    valor_decimal = (alfabeto.index(entrada) + 1)
    print(f"A letra {entrada} está na posição {valor_decimal} do alfabeto.")
    return valor_decimal

def par_impar(valor_decimal):
    if valor_decimal % 2 == 0:
        print(f"O valor {valor_decimal} é par")
    else:
        print(f"O valor {valor_decimal} é ímpar")

par_impar(letra(input("Digite uma letra do alfabeto: ")))