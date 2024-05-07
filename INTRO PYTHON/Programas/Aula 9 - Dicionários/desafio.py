pacientes = {
    "10001": {"Nome" : "José", "Idade" : 39, "Telefone" : "98123-1375"},
    "10002": {"Nome" : "Érica", "Idade" : 19, "Telefone" : "98123-5464"},
    "10003": {"Nome" : "Joana", "Idade" : 26, "Telefone" : "98546-7159"},
}

médicos = {
    "90001": {"Nome" : "Epaminondas", "Idade" : 59, "Telefone" : "98555-5555", "Especialidade" : "Urologia"},
    "90002": {"Nome" : "Hermione", "Idade" : 49, "Telefone" : "98555-6666", "Especialidade" : "Ginecologia"},
    "90003": {"Nome" : "Maria das Graças", "Idade" : 71, "Telefone" : "98555-7777", "Especialidade" : "Neurocirurgia"},
    "90004": {"Nome" : "Carlos Fernando", "Idade" : 47, "Telefone" : "98555-8888", "Especialidade" : "Fisioterapia"},
}

agendamentos = {
    "AG0001" : {"Paciente" : pacientes["10001"]["Nome"], "Médico" : médicos["90001"]["Nome"], "Data" : "10/12/2024", "Hora" : "09:40"},
    "AG0002" : {"Paciente" : pacientes["10002"]["Nome"], "Médico" : médicos["90002"]["Nome"], "Data" : "07/10/2024", "Hora" : "13:00"},
    "AG0003" : {"Paciente" : pacientes["10003"]["Nome"], "Médico" : médicos["90003"]["Nome"], "Data" : "18/11/2024", "Hora" : "15:30"},
    "AG0004" : {"Paciente" : pacientes["10003"]["Nome"], "Médico" : médicos["90003"]["Nome"], "Data" : "15/09/2024", "Hora" : "10:20"},
    "AG0005" : {"Paciente" : pacientes["10002"]["Nome"], "Médico" : médicos["90004"]["Nome"], "Data" : "08/10/2024", "Hora" : "14:00"},
}

for i, j in agendamentos.items():
    print(f"{i} : {j}")

print("Programa de Agendamentos de Consulta")
while True:
    opção = str(input("Digite 1 para entrar novos pacientes, 2 para entrar novos médicos, 3 para criar novo agendamento, 4 para consultar todos agendamentos e 0 para sair: "))
    if opção == "1":
        while True:
            chave = int(input("Digite o CÓDIGO do novo paciente (digite 0 para sair): "))
            if chave == 0:
                break
            nome = str(input("Digite o NOME do novo paciente: "))
            idade = str(input("Digite a IDADE do novo paciente: "))
            telefone = str(input("Digite o TELEFONE do novo paciente: "))
            pacientes[chave] = {"Nome": nome, "Idade": idade, "Telefone" : telefone}
    elif opção == "2":
        while True:
            chave = int(input("Digite o CÓDIGO do novo médico (digite 0 para sair): "))
            if chave == 0:
                break
            nome = str(input("Digite o NOME do novo médico: "))
            idade = str(input("Digite a IDADE do novo médico: "))
            telefone = str(input("Digite o TELEFONE do novo médico: "))
            pacientes[chave] = {"Nome": nome, "Idade": idade, "Telefone" : telefone}