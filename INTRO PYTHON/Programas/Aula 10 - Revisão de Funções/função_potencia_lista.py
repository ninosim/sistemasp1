def potencia (x):
    quadrado = x ** 2
    cubo = x ** 3
    return quadrado, cubo

lista = [(potencia(int(input("Digite um número: "))))]

print(lista)