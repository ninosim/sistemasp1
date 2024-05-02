
''' 1) Crie um programa que tenha dois dicionários sendo eles, feminino e masculino.
2) Receba os dados de clientes (nome, sexo e idade), até que o usuário não queira mais receber dados (pelo menos 10 clientes)
3) Se for do sexo feminino, inclua os dados no dicionário feminino. O mesmo para o masculino.
4) Por fim, informe todos os dados cadastrados para cada sexo.'''


masc = {}
fem = {}

print("Programa de Cadastro de Clientes")

while True:
    nome = input("Digite o nome do/a cliente (digite 0 para parar o cadastro): ")

    if nome == "0":
        break

    sexo = input("Digite M para cliente do sexo Masculino e F para Feminino: ").upper()

    if sexo == "M":
        idade = int(input("Digite a idade do cliente: "))
        masc[nome] = {"Idade" : idade}
    elif sexo == "F":
        idade = int(input("Digite a idade do cliente: "))
        fem[nome] = {"Idade" : idade}
    else:
        print("Sexo inválido, digite M ou F.")

print(f"Os clientes do sexo masculino são: {masc}")
print(f"Os clientes do sexo feminino são: {fem}")