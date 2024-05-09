def conversao (valor, frete):
    cotacao_dolar = 5.09
    valor_real = valor * cotacao_dolar
    frete_real = frete * cotacao_dolar
    total = valor_real + frete_real
    return total

print(f"Produtos disponíveis:\n Notebook: US$ 750\n Smartwatch: US$ 250")
escolha = int(input("Digite 1 para comprar o Notebook e 2 para comprar o Smartwatch: "))
if escolha == 1:
    valor = 750
    local = int(input("Escolha o país para o envio (digite 1 para Brasil e 2 para Argentina): "))
    if local == 1:
        frete = 52
        destino = "Brasil"
    elif local == 2:
        frete = 75
        destino = "Argentina"
    else:
        print("Escolha inválida. Tente novamente.")
    print(f"O seu produto custa US$ {valor}. O frete para o país escolhido ({destino}) custa US$ {frete}. O valor total do seu pedido é de: US$ {valor + frete} ")
elif escolha == 2:
    valor = 250
    local = int(input("Escolha o país para o envio (digite 1 para Brasil e 2 para Argentina): "))
    if local == 1:
        frete = 52
        destino = "Brasil"
    elif local == 2:
        frete = 75
        destino = "Argentina"
    else:
        print("Escolha inválida. Tente novamente.")
    print(f"O seu produto custa US$ {valor}. O frete para o país escolhido ({destino}) custa US$ {frete}. O valor total do seu pedido é de: US$ {valor + frete} ")
else:
    print("Escolha inválida. Tente novamente.")

total = conversao(valor, frete)
print(f"O valor total da sua compra (convertido em reais) é: R$ {total}")