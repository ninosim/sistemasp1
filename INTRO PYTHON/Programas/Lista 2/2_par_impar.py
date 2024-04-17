print('Exibidora de Números Pares/Ímpares')
x = int(input('Digite um valor inteiro: '))
y = float(x)
if y % 2 == 0:
    for i in range(0 , x+1, 2):
        print(i)
else:
    for i in range(1 , x+1, 2):
        print(i)