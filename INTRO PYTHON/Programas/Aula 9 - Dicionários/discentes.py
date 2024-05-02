# Crie um dicionário chamado alunos com os campos "matrícula", "nome", "idade,"sexo" e "curso". Inclua pelo menos 5 alunos.

# O primeiro valor é a Chave, os seguintes são os campos.

alunos = {
    20240001 : {"Nome" : "André", "Idade" : 35, "Sexo" : "Masculino", "Curso" : "Direito"},
    20240002 : {"Nome" : "Adriana", "Idade" : 22, "Sexo" : "Feminino", "Curso" : "Engenharia"},
    20240003 : {"Nome" : "Cláudia", "Idade" : 27, "Sexo" : "Feminino", "Curso" : "Arquitetura"},
    20240004 : {"Nome" : "Carine", "Idade" : 25, "Sexo" : "Feminino", "Curso" : "Letras"},
    20240005 : {"Nome" : "Thiago", "Idade" : 29, "Sexo" : "Masculino", "Curso" : "Letras"},
}

# Acessa o campo "Nome" da chave 20240003 e altera seu valor para "Gustavo":

alunos[20240003]["Nome"] = "Gustavo"

# Acrescenta uma nova chave e seus valores correspondentes:

alunos.update({20240006 : {"Nome" : "Carlos", "Idade" : 20, "Sexo" : "Masculino", "Curso" : "Educação Física"}})

# Para acrescentar várias chaves, o ideal é criar um novo dicionário e acrescentá-lo ao primeiro:

novos = {
    20240007 : {"Nome" : "Odmir", "Idade" : 25, "Sexo" : "Masculino", "Curso" : "Design"},
    20240008 : {"Nome" : "Ariel", "Idade" : 26, "Sexo" : "Masculino", "Curso" : "Design"},
    20240009 : {"Nome" : "Lud", "Idade" : 27, "Sexo" : "Masculino", "Curso" : "Biologia"},
    20240010 : {"Nome" : "Clarice", "Idade" : 33, "Sexo" : "Masculino", "Curso" : "Letras"},
} 
alunos.update(novos)

# Para percorrer um dicionário, usamos for e a função .items()

for i, j in alunos.items():
    print(f"{i} : {j}")

