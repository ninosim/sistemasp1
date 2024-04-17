print('Calculadora de Soma e Par/Ímpar')
x = int(input('Digite o primeiro valor:'))
y = int(input('Digite o segundo valor:'))
z = float(x+y)


if z % 2 == 0:
    print('A soma dos dois valores é:', z , ', que é um número PAR')
else:
    print('A soma dos dois valores é:', z, ', que é um número ÍMPAR')