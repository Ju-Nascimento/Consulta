from datetime import datetime

# Lista para armazenar as especialidades médicas
especialidades = ["Psicologo", "Psiquiatra", "Fonoaudiologo"]

class SelecionadorDataHora:
    def __init__(self):
        self.data_hora_selecionada = None

    def selecionar_data_hora(self):
        while True:
            data_hora_str = input("Insira a data e hora da consulta (dd/mm/aaaa hh:mm): ")
            try:
                data_hora = datetime.strptime(data_hora_str, '%d/%m/%Y %H:%M')
                self.data_hora_selecionada = data_hora
                break
            except ValueError:
                print("Formato de data e hora inválido. Use o formato correto (dd/mm/aaaa hh:mm) e tente novamente.")

    def obter_data_hora_selecionada(self):
        return self.data_hora_selecionada

def marcarConsulta(pacientes, consultas):
    if not pacientes:
        print("Não há pacientes cadastrados.")
        return

    print("Escolha um paciente para a consulta:")
    for i, paciente in enumerate(pacientes):
        print(f"{i + 1} - {paciente['nome']}")

    paciente_index = int(input("Escolha o número do paciente: ")) - 1
    if paciente_index < 0 or paciente_index >= len(pacientes):
        print("Paciente inválido.")
        return

    selecionador = SelecionadorDataHora()
    selecionador.selecionar_data_hora()
    data_hora_selecionada = selecionador.obter_data_hora_selecionada()

    print("Escolha a especialidade médica:")
    for i, especialidade in enumerate(especialidades):
        print(f"{i + 1} - {especialidade}")

    especialidade_index = int(input("Escolha o número da especialidade: ")) - 1
    if especialidade_index < 0 or especialidade_index >= len(especialidades):
        print("Especialidade inválida.")
        return

    consulta = {
        'paciente': pacientes[paciente_index],
        'data_hora': data_hora_selecionada,
        'especialidade': especialidades[especialidade_index]
    }
    consultas.append(consulta)
    print(f"Consulta marcada para {pacientes[paciente_index]['nome']} em {data_hora_selecionada} com especialidade {especialidades[especialidade_index]}.")

def consultasAgendadas(consultas):
    if not consultas:
        print("Não há consultas agendadas.")
        return

    for consulta in consultas:
        print(f"{consulta['paciente']['nome']} - {consulta['data_hora']} - {consulta['especialidade']}")

def cancelarConsulta(consultas):
    if not consultas:
        print("Não há consultas para cancelar.")
        return

    print("Escolha uma consulta para cancelar:")
    for i, consulta in enumerate(consultas):
        print(f"{i + 1} - {consulta['paciente']['nome']} - {consulta['data_hora']} - {consulta['especialidade']}")

    consulta_index = int(input("Escolha o número da consulta para cancelar: ")) - 1
    if consulta_index < 0 or consulta_index >= len(consultas):
        print("Consulta inválida.")
        return

    consulta_cancelada = consultas.pop(consulta_index)
    print(f"Consulta de {consulta_cancelada['paciente']['nome']} cancelada.")
