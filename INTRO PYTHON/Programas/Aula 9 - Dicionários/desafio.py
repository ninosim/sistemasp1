pacientes = {
    10001: {"Nome" : "José", "Idade" : 39, "Telefone" : "98123-1375"},
    10002: {"Nome" : "Érica", "Idade" : 19, "Telefone" : "98123-5464"},
    10003: {"Nome" : "Joana", "Idade" : 26, "Telefone" : "98546-7159"},
}

médicos = {
    90001: {"Nome" : "Epaminondas", "Idade" : 59, "Telefone" : "98555-5555", "Especialidade" : "Urologia"},
    90002: {"Nome" : "Hermione", "Idade" : 49, "Telefone" : "98555-6666", "Especialidade" : "Ginecologia"},
    90003: {"Nome" : "Maria das Graças", "Idade" : 71, "Telefone" : "98555-7777", "Especialidade" : "Neurocirurgia"},
    90004: {"Nome" : "Carlos Fernando", "Idade" : 47, "Telefone" : "98555-8888", "Especialidade" : "Fisioterapia"},
    }

agendamentos = {
    "AG0001" : {"Paciente" : 10001, "Médico" : 90001, "Data" : "10/12/2024", "Hora" : "09:40"},
    "AG0002" : {"Paciente" : 10002, "Médico" : 90002, "Data" : "07/10/2024", "Hora" : "13:00"},
    "AG0003" : {"Paciente" : 10003, "Médico" : 90003, "Data" : "18/11/2024", "Hora" : "15:30"},
    "AG0004" : {"Paciente" : 10002, "Médico" : 90002, "Data" : "15/09/2024", "Hora" : "10:20"},
    "AG0005" : {"Paciente" : 10001, "Médico" : 90003, "Data" : "08/10/2024", "Hora" : "14:00"},
}

for i, j in agendamentos.items():
    print(f"{i} : {j}")