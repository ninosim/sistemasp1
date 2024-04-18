# 2o Crie uma lista que receba valores inteiros do usuário até que o usuário queira parar de inserir valores
# (colocar uma condição de parada), faça a soma e retorne o resultado para o usuário.

entrada = 1
lista = []
soma = 0

while entrada != 0:
    entrada = int(input("Digite o valor a ser somado (digite 0 para finalizar a soma): "))
    lista.append(entrada)
    print(lista)

print(f"A soma dos valores digitados é: {sum(lista)}")