z = int(input('Calculadora de Sequência Fibonacci. \nDigite o valor máximo: '))
x = 0
y = 1


while x <= z:
    print(x, end=', ')
    x = x + y
    if y <= z:
        print(y , end=', ')
        y = x + y