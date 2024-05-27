#FALTA FAZER:
#CONTROLE DE ESTOQUE (gerar uma lista com o estoque atual , como aquela lista de produtos e preços)
#ESCOLHER UM VENDEDOR ANTES DE COMPRAR
#CÁLCULO DE COMISSÃO E IMPOSTO SOBRE VENDAS


#Estabelecendo as Listas
lista_produtos = [['Mouse', 45.0, 21], ['Teclado', 89.0, 18], ['Tablet', 890.0, 12], ['Monitor', 1050.0, 8]]
lista_clientes = [['Camilly', '(83)99999-9991'], ['Márcio', '83999999993']]
lista_vendedores = [['Ellen', '(83)99999-9992', 0], ['Nino', '83999999999', 69.0]]
#O terceiro valor do vendedor é a comissão de vendas

carrinho = []

while True:

    #Menu Inicial
    print(f'{"=-"*5}{"TECH POINT ELETRÔNICOS-"}{"=-"*5}')
    print('-'*35)
    print(f'{"O QUE DESEJA FAZER?":^35}')
    print('-'*35)
    print('[1] Cadastrar Produtos\n[2] Cadastrar Cliente\n[3] Cadastrar Vendedor\n[4] Escolher Produtos para Compra\n[5] Ir para Carrinho de Compras\n[6] Relatório de Vendas\n[7] Sair')
    print('-'*35)
    opcao=int(input('Digite a opção escolhida: '))

    # Caso Escolha Cadastrar Produtos
    if opcao == 1:
        dados = []
        while True:
            produto = str(input('Produto: '))
            preco = float(input('Preço: '))
            quantidade = int(input('Quantidade: '))
            dados.append(produto)
            dados.append(preco)
            dados.append(quantidade)
            lista_produtos.append(dados[:])
            dados.clear()
            parar = str(input('Deseja Continuar? [S/N]: '))
            if parar in 'Nn':
                break

    # Caso escolha Cadastrar Cliente
    elif opcao == 2:
        dados = []
        while True:
            nome = str(input('Nome do Cliente: '))
            telefone = str(input('Telefone do Cliente: '))
            dados.append(nome)
            dados.append(telefone)
            lista_clientes.append(dados[:])
            dados.clear()
            parar = str(input('Deseja Continuar? [S/N]: '))
            if parar in 'Nn':
                break

    # Caso escolha Cadastrar Vendedor
    elif opcao == 3:
        dados = []
        while True:
            nome = str(input('Nome do Vendedor: '))
            telefone = str(input('Telefone do Vendedor: '))
            comissao = float(input('Comissão anterior (0 se não houver): '))
            dados.append(nome)
            dados.append(telefone)
            dados.append(comissao)
            lista_vendedores.append(dados[:])
            dados.clear()
            parar = str(input('Deseja Continuar? [S/N]: '))
            if parar in 'Nn':
                break

    # Caso Escolha Realizar Compras
    elif opcao == 4:
        while True:

            #Mostra Lista de Produtos e Preços
            print('-' * 37)
            print(f'{"LISTA DE PRODUTOS E PREÇOS":^37}')
            print('-' * 40)
            for pos in range(len(lista_produtos)):
                print('{:.<3}'.format(pos+1), end='')
                print('{:.<30}'.format(lista_produtos[pos][0]), end='')
                print('R$ {:.>.2f}'.format(lista_produtos[pos][1]))
            print('-' * 40)

            # Pergunta Qual Produto Quer Comprar
            prod= int(input('Qual produto o cliente quer comprar? '))

            # Busca o produto na lista_produtos, Informa a quantidade e pergunta quantos o cliente quer comprar

            print(f"A quantidade de {lista_produtos[prod-1][0]} no estoque é {lista_produtos[prod-1][2]}.")
            quant = int(input('Qual a quantidade deseja comprar? '))
            print(f'{quant} {lista_produtos[prod-1][0]} adicionado(s) no carrinho de compras.')

            # Atualiza a quantidade do produto na listas, após a compra, e adiciona o produto ao carrinho
            lista_produtos[prod-1][2] = lista_produtos[prod-1][2] - quant
            car=[]
            car.append(lista_produtos[prod-1][0])
            car.append(lista_produtos[prod-1][1])
            car.append(quant)
            carrinho.append(car[:])
            print(f'O carrinho de compras agora contém {carrinho}')
            car.clear()

            # Pergunta se Quer continuar comprando
            parar = str(input('Deseja Comprar mais Produtos? [S/N]: '))
            if parar in 'Nn':
                break

    # Caso Escolha Ir para Carrinho de Compras
    elif opcao == 5:
        total = itens = 0
        print(carrinho) # TESTE - APAGAR QUANDO ACABAR O CÓDIGO
        print('=' * 37)
        print(f'{"CARRINHO DE COMPRAS":^37}')
        print('=' * 40)
        for pos in range(len(carrinho)):
            print('{:.<3}'.format(pos + 1), end='')
            print('{:.<30}'.format(carrinho[pos][0]), end='')
            print('R$ {:.>.2f}'.format(carrinho[pos][1]), end='')
            print('{:.>12.2f} unid.'.format(carrinho[pos][2]))

            total=total+(carrinho[pos][1]*carrinho[pos][2])
            itens=itens+(carrinho[pos][2])
        print('-' * 61)
        print('{:.<33}'.format('TOTAL'), end='')
        print('R$ {:.>.2f}'.format(total), end='')
        print('{:.>10.2f} itens.'.format(itens))
        print('=' * 40)

    # Caso Escolha Relatório de Vendas
    elif opcao == 6:
        print('x')

    # Caso Escolha Sair
    elif opcao == 7:
        for produto in lista_produtos:
            print(produto)
        print(carrinho)
        break
    else:
        print('Opção Inválida. Tente Novamente.\n')
        continue

#ÁREA DE TESTES - Isso será apagado quando terminar o código. Por enquanto serve só pra testes.
for produto in lista_produtos:
    print(produto)
print(carrinho)
