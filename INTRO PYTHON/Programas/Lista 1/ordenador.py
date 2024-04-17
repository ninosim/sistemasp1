# 6.	Escreva um código que receba 3 números inteiros e os exiba em ordem crescente.

print('Ordenador de Números')

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

if a > b and a > c:
	a = top
elif b > a and b > c:
	b = top
else:
	c = top

if a < b and a < c:
	a = bot
elif b < a and b < c:
	b = bot
else:
	c = bot

if a != top and a != bot:
	a = mid

if b != top and b != bot:
	b = mid

if b != top and b != bot:
	b = mid

print('A ordem crescente dos números digitados é: ', top, mid, bot)