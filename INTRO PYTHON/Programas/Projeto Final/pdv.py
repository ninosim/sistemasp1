print("Seja bem-vindo ao Ponto de Venda!")

produtos = {}
carrinho = {}

while True:
    cliente_ou_fornecedor = int(input("Você é cliente ou fornecedor? Digite 1 para Cliente e 2 para Fornecedor: "))
    if cliente_ou_fornecedor == 1:
        print("Boas compras!")
        while True:
            print(produtos)
            compra = int(input("Digite o código do produto desejado para acrescentá-lo ao seu carrinho de compras (Digite 0 para finalizar a compra): "))
            if compra == 0:
                print("Você digitou 0 e está sendo encaminhado para a finalização da compra.")
                # ACRESCENTAR toda a mecânica de listar carrinho e descontar os produtos do estoque.
                break
            elif compra in (produtos):
                quant = int(input("Quantas unidades desse produto você deseja comprar? "))
                # ESCREVER código para acrescentar o produto (chave e valores) ao dicionário "carrinho"
            else:
                print("Código de produto inválido. Tente novamente.")
                continue
    elif cliente_ou_fornecedor == 2:
        print("Seja bem-vindo, fornecedor ou estoquista!")
        while True:
            print(produtos)
            menu_fornecedor = int(input("O que você deseja fazer? Digite 1 para acrescentar um produto, 2 para, 0 para sair: "))
            if menu_fornecedor == 1:
                produto_nome = str(input("Qual o nome do produto? "))
                produto_preço = float(input("Qual o preço do produto? "))
                produto_quantidade = int(input("O produto tem quantas unidades disponíveis? "))
                lista_chaves = list(produtos.keys())
                codigo_produto_novo = (lista_chaves[-1]) + 1
                produto_novo = {"Nome" : produto_nome, "Preço" : produto_preço, "Estoque" : produto_quantidade}
                #Acrescentar código para puxar o código do último produto e acrescentar 1 para servir como chave do produto_novo
                produtos.update(codigo_produto_novo : produto_novo)