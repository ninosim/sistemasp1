# 3.	Escreva um código que receba a sua idade e retorne o ano do seu nascimento.

from datetime import date

today = date.today()

print('Calculador de Ano de Nascimento')
idade = int(input('Digite a sua idade: '))

print('Você nasceu no ano', (today.year - idade))