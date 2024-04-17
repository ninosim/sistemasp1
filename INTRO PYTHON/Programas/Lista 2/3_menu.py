x = int(input('Bem-vindo ao menu. \n Digite 1 para continuar; \n Digite 2 para sair: '))


if x != 1 and x != 2:
    print('Você digitou um valor inválido. Tente novamente.')


while x == 1:
    x = int(input('Bem-vindo ao menu. \n Digite 1 para continuar; \n Digite 2 para sair: '))
    if x != 1 and x != 2:
        print('Você digitou um valor inválido. Tente novamente.')