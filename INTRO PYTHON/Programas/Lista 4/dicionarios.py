'''
1) Crie um programa que tenha dois dicionários sendo eles, feminino e masculino.
2) Receba os dados de clientes (nome, sexo e idade), até que o usuário não queira mais receber dados (pelo menos 10 clientes)
3) Se for do sexo feminino, inclua os dados no dicionário feminino. O mesmo para o masculino.
4) Por fim, informe todos os dados cadastrados para cada sexo.'''

print("Cadastro de Clientes")

masc = {}
fem = {}

while True:
    cliente = input("Digite o nome do/a cliente:")
    sexo = input("Digite M para sexo masculino ou F para feminino:")
    idade = input("Digite a idade do/a cliente:")
    if sexo == "M"


clientes = {
	1001:{'nome': 'João', 'idade': 37} ,
	1002:{'nome': 'Maria', 'idade': 29} ,
	1003:{'nome': 'José', 'idade': 99}
}

# Retorna todos os dados associados à chave 1001
print(clientes[1001])

# Retorna apenas o nome associado à chave 1001
print(clientes[1001]['nome'])

print(f"O cliente {clientes[1001]['nome']} tem {clientes[1001]['idade']} anos.")
print(f"O cliente {clientes[1002]['nome']} tem {clientes[1002]['idade']} anos.")
print(f"O cliente {clientes[1003]['nome']} tem {clientes[1003]['idade']} anos.")