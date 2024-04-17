print('Calculadora Tabajara 3.000')

z = float(input('Digite 1 para realizar uma Soma, 2 para Subtração, 3 para Multiplicação e 4 para Divisão: '))

if z == 1:
	print('Você escolheu Soma')
elif z == 2:
	print('Você escolheu Subtração')
elif z == 3:
	print('Você escolheu Multiplicação')
elif z == 4:
	print('Você escolheu Divisão')
else:
	print('Operação Inválida, tente novamente.')

x = float(input('Digite o primeiro número: '))

y = float(input('Digite o segundo número: '))

if z == 1:
	print('O resultado é igual a: ', x + y)
elif z == 2:
	print('O resultado é igual a: ', x - y)
elif z == 3:
	print('O resultado é igual a: ', x * y)
elif z == 4:
	print('O resultado é igual a: ', x / y)
else:
	print('Operação Inválida, tente novamente.')