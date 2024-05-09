import f_biblioteca 

nome = str(input("Digite o nome do usuário: "))
nascimento = int(input("Digite o ano de nascimento do usuário: "))
print(f"O nome do usuário tem {f_biblioteca.contagem(nome)} letras. Em 31/12/2024 ele terá {f_biblioteca.idade(nascimento)} anos.")