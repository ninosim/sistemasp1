lista = []

for i in range(5):
    lista.append(int(input("Digite um valor: ")))

def quadrado(valor):
    return valor * valor

lista2 = list(map(quadrado,lista))
print("Lista original: ", lista)
print("Lista do quadrado: ", lista2)