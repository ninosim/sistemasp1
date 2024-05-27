'''Crie uma lista com os valores (23, 32, 64, 18, 9, 51, 67, 90).
1) Os ordene em ordem crescente e imprima
2) Os ordene em ordem decrescente e imprima
3) Imprima o valor da soma de todos os valores
4) Imprima o tamanho da lista
5) Imprima o último valor'''

lista = [23, 32, 64, 18, 9, 51, 67, 90]
print(f"Lista original: {lista}")
lista.sort()
print(f"Lista ordenada em ordem crescente: {lista}")
lista.sort(reverse= True)
print(f"Lista Ordenada em ordem decrescente: {lista}")
print(f"Soma de todos os valores da lista: {sum(lista)}")
print(f"A lista tem {len(lista)} elementos.")
print(f"O último elemento da lista é {lista.pop()}")