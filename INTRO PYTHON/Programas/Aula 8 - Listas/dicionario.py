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