# Para cada fruta, nome, preço e quantidade em estoque

estoque = {}

print("Programa Administrador de Frutas")

while True:
    fruta = str(input("Digite o nome da fruta(digite 0 para sair): "))
    if fruta == "0":
        break
    preço = float(input("Digite o preço da fruta: "))
    quantidade = int(input("Digite a quantidade de frutas em estoque: "))

    estoque[fruta] = {
        "Preço" : preço,
        "Estoque" : quantidade
    }

print(estoque)