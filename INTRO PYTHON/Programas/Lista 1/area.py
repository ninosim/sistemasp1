# 4.	Escreva um código que receba o valor do raio de uma circunferência e retorne a área desta circunferência. 

import math

print('Calculadora de Área de Circunferências (A = π.r²)')

raio = float(input('Digite o valor do RAIO da circunferência: '))

A = (math.pi * (raio * raio))

print('A área da circunferência é igual a: ', A)