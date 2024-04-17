# 7.	Escreva um código que receba um valor inteiro e diga se ele é divisível por cinco.

print('Determinador de Divisão por 5')

a = int(input('Digite o valor inteiro: '))

b = int(a/5)

if (b * 5) == a:
	print('O número é divisível por 5.')
else:
	print('O número NÃO é divisível por 5.')