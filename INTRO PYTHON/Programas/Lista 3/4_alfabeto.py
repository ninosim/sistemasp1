# 4o Crie uma função que receba como parâmetro uma letra do alfabeto e retorne o valor decimal respectivo a sua ordem no alfabeto.
# Ex.: Caso o atributo passado seja a letra “H”, o retorno deverá ser o número 8.
# O resultado da função deverá ser passado como atributo para outra função que retornará:
# Caso o valor seja par, retornar os valores pares de 2 ao valor passado
# Caso seja ímpar, retornar os valores ímpares de 1 ao valor passado

def posicao_alfabeto(entrada):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    posicao = (alfabeto.index(entrada.lower()) + 1)
    return posicao

def par_impar(posicao):
    if posicao % 2 == 0:
        print(f"O valor {posicao} é par e os números pares anteriores a ele são: ")
        for i in range(2, posicao, 2):
            print(i)
    else:
        print(f"O valor {posicao} é ímpar e os números ímpares anteriores a ele são: ")
        for i in range(1, posicao, 2):
            print(i)

letra = str(input("Digite uma letra do alfabeto: "))

posicao = posicao_alfabeto(letra)

print(f"A letra {letra} está na posição {posicao} do alfabeto.")

par_impar(posicao)