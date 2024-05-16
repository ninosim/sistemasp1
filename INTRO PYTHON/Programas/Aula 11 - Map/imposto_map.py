def imposto (valor):
    return valor * 1.1

valor_original = [1000, 1500, 1250, 2500]

valor_com_imposto = list(map(imposto,valor_original))
total = map(sum,valor_original)

print("Valores originais: ", valor_original)
print("Valores com 10 por centro de imposto: ", valor_com_imposto)