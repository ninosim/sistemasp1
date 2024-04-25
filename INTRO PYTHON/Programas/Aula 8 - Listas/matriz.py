lista0 = []
lista0.extend(["a", "b"])
print(lista0)

# .extend acrescenta os itens a uma lista em novas posições 

lista0.append(["c", "d"])
print(lista0)
print(lista0[2][0])

# .append acrescenta os itens À ÚLTIMA POSIÇÃO de uma lista
#  Isso pode adicionar uma lista inteira em uma única posição, efetivamente criando uma lista dentro de uma lista (uma matriz)

lista1 = ["a", "b"]
print(lista1)
lista2 = ["c", "d"]
print(lista2)
lista1.extend(lista2)
print(lista1)

lista3 = (lista1 + lista2)
print(lista3)