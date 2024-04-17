# 3o Crie uma lista com os valores “GM”, “FIAT”, “Volkswagem”, “Ford”, “Honda”, “Toyota”, “Gurgel”, “Dodge”. Após a lista estar pronta:
# a) Adicione as marcas “Hyundai”, “BMW” e “Nissan”, nas posições 3, 4 e 5, respectivamente;
# b) Altere o nome da marca “GM” para “Chevrolet”;
# c) Remova a marca “Gurgel”
# d) Reorganize a lista por ordem alfabética (Extra)

fabricantes = ["GM", "Fiat", "Volkswagem", "Ford", "Honda", "Toyota", "Gurgel", "Dodge"]
print(f"Lista original: {fabricantes}")
fabricantes.insert(3, "Hyundai")
fabricantes.insert(4, "BMW")
fabricantes.insert(5, "Nissan")

fabricantes[1] = "Chevrolet"
fabricantes.remove("Gurgel")

print(f"Lista com adição de Chevrolet e remoção de Gurgel: {fabricantes}")

fabricantes.sort()
print(f"Lista Ordenada Alfabeticamente: {fabricantes}")