def addPaciente(pacientes):
    nome = input("Nome do paciente: ")
    telefone = input("Telefone do paciente: ")
    email = input("Email do paciente: ")
    cpf = input("CPF do paciente: ")

    paciente = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'cpf': cpf
    }
    pacientes.append(paciente)
    print(f"Paciente {nome} cadastrado com sucesso.")
