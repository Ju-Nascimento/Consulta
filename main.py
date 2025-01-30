import consulta
import paciente

def menu():
    print("1 - Cadastrar paciente")
    print("2 - Nova consulta")
    print("3 - Consultas agendadas")
    print("4 - Cancelar consultas")
    print("5 - Sair")

if __name__ == '__main__':
    pacientes = []  # Lista para armazenar pacientes cadastrados
    consultas = []  # Lista para armazenar consultas agendadas
    
    while True:
        menu()
        opcao = int(input("Escolha uma opção: "))
        
        match opcao:
            case 1:
                paciente.addPaciente(pacientes)
            case 2:
                consulta.marcarConsulta(pacientes, consultas)
            case 3:
                consulta.consultasAgendadas(consultas)
            case 4:
                consulta.cancelarConsulta(consultas)
            case 5:
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")
