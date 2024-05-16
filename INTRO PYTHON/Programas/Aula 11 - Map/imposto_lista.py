def imposto (valor):
    return valor * 1.1

valor_original = [1000, 1500, 1250, 2500]

valor_com_imposto = []

for valor in valor_original:
    valor_com_imposto.append(imposto(valor))

print("Valores originais:", valor_original)
print("Valores com 10 por centro de imposto: ", valor_com_imposto)