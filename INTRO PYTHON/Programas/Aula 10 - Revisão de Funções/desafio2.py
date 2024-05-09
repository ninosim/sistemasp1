# CRIA UMA LISTA COM AS CHAVES DE UM DICIONÁRIO
# chaves_lista = list(pacientes.keys())
# PUXA O VALOR DO DICIONÁRIO USANDO O INDEX DA LISTA COMO REFERÊNCIA
# recente = pacientes[chaves_lista[-1]]

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
    "AG0001" : {"Paciente" : pacientes[10001]["Nome"], "Médico" : médicos[90001]["Nome"], "Data" : "10/12/2024", "Hora" : "09:40"},
    "AG0002" : {"Paciente" : pacientes[10002]["Nome"], "Médico" : médicos[90002]["Nome"], "Data" : "07/10/2024", "Hora" : "13:00"},
    "AG0003" : {"Paciente" : pacientes[10003]["Nome"], "Médico" : médicos[90003]["Nome"], "Data" : "18/11/2024", "Hora" : "15:30"},
    "AG0004" : {"Paciente" : pacientes[10003]["Nome"], "Médico" : médicos[90003]["Nome"], "Data" : "15/09/2024", "Hora" : "10:20"},
    "AG0005" : {"Paciente" : pacientes[10002]["Nome"], "Médico" : médicos[90004]["Nome"], "Data" : "08/10/2024", "Hora" : "14:00"},
}

while True:
    print("Programa de Agendamentos de Consulta")
    opção = str(input("Digite 1 para cadastrar novos pacientes, \n2 para cadastrar novos médicos, \n3 para cadastrar novos agendamentos, \n4 para consultar os pacientes cadastrados, \n5 para consultar os médicos cadastrados, \n6 para consultar os agendamentos cadastrados e \n0 para sair: \n"))
    if opção == "1":
        while True:
#ALTERAR ISSO    chave = pacientes.popitem()[-1] + 1
#            chave = str(input("Digite o CÓDIGO do novo paciente (digite 0 para sair): "))
            nome = str(input("Digite o NOME do novo paciente (digite 0 para sair): "))
            if nome == "0":
                break
            idade = str(input("Digite a IDADE do novo paciente: "))
            telefone = str(input("Digite o TELEFONE do novo paciente: "))
            pacientes[chave] = {"Nome": nome, "Idade": idade, "Telefone" : telefone}
            print(f"Novo paciente cadastrado: {pacientes[chave]}")
    elif opção == "2":
        while True:
#ALTERAR ISSO            chave = int(médicos.popitem()[-1] + 1)
#            chave = str(input("Digite o CÓDIGO do novo médico (digite 0 para sair): "))
            nome = str(input("Digite o NOME do novo médico (digite 0 para sair): "))
            if nome == "0":
                break
            idade = str(input("Digite a IDADE do novo médico: "))
            telefone = str(input("Digite o TELEFONE do novo médico: "))
            especialidade = str(input("Digite a ESPECIALIDADE do novo médico: "))
            médicos[chave] = {"Nome": nome, "Idade": idade, "Telefone" : telefone, "Especialidade" : especialidade}
            print(f"Novo médico cadastrado: {médicos[chave]}")
    elif opção == "3":
        while True:
#ALTERAR ISSO            chave = int(pacientes.popitem()[-1] + 1)
#            chave = str(input("Digite o CÓDIGO do novo agendamento (digite 0 para sair): "))
            codigo_paciente = int(input("Digite o CÓDIGO do paciente (digite 0 para sair): "))
            if codigo_paciente == 0:
                break
            elif codigo_paciente not in pacientes.keys():
                print("Código de paciente inválido, tente novamente.")
                continue
            codigo_medico = int(input("Digite o CÓDIGO do médico: "))
            if codigo_medico not in médicos.keys():
                print("Código de médico inválido, tente novamente.")
                continue
            data = str(input("Digite a DATA do agendamento: "))
            hora = str(input("Digite a HORA do agendamento (formato 24h): "))
            agendamentos[chave] = {"Paciente": pacientes[codigo_paciente]["Nome"], "Medico": médicos[codigo_medico]["Nome"], "Data" : data, "Hora" : hora}
            print(f"Novo agendamento cadastrado: {agendamentos[chave]}")
    elif opção =="4":
        print("PACIENTES CADASTRADOS:")
        for i, j in pacientes.items():
            print(f"{i} : {j}")
    elif opção =="5":
        print("MÉDICOS CADASTRADOS:")
        for i, j in médicos.items():
            print(f"{i} : {j}")
    elif opção =="6":
        print("AGENDAMENTOS CADASTRADOS:")
        for i, j in agendamentos.items():
            print(f"{i} : {j}")
    elif opção =="0":
        print("Programa encerrado. Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.")