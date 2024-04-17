log = input('Bem-vindo ao Sistema UNIESP. \nDigite o seu login: ')
sen = input('Digite a sua senha: ')


if log == 'admin' and sen == 'admin':
    print('Você está logado, usuário', log)
else:
    print('Login ou senha incorretos. Tente novamente.')