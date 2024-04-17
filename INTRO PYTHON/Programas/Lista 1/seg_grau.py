# Escreva um código que receba 3 valores inteiros (a, b e c). Utilize  esses valores para encontrar o valor de delta. Caso o valor de delta seja menor que zero, informar que a equação não possui raízes reais. Se for maior ou igual a zero, encontre e informe os valores de x1 e x2. Para raiz quadrada precisaremos importar a biblioteca “math” e usar o comando math.sqrt().

import math

print('Bem-vindo à calculadora de equações de segundo grau Δ = b² – 4ac.')

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = ((b*b) - 4*(a*c))

print('O delta é igual a: ', delta)

if delta < 0:
	print ('A equação não possui raízes reais.')
else:
	x1 = ((b*-1) + math.sqrt(delta))/2*a
	x2 = ((b*-1) - math.sqrt(delta))/2*a
	print ('A equação possui as seguintes raízes:', x1,' e ', x2)