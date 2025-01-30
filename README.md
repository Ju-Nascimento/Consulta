# Sistema de Agendamento de Consultas Médicas

Este projeto implementa um sistema simples de agendamento de consultas médicas em Python. O sistema permite cadastrar pacientes, marcar consultas, listar consultas agendadas e cancelar consultas.

## Estrutura do Projeto

O projeto é composto por três arquivos principais:

*   `main.py`: Arquivo principal que contém o menu interativo e a lógica principal do sistema.
*   `paciente.py`: Arquivo que contém funções para adicionar pacientes.
*   `consulta.py`: Arquivo que contém funções para marcar consultas, listar consultas agendadas e cancelar consultas.

## Como Executar

1.  Clone este repositório.
2.  Certifique-se de ter o Python instalado em seu sistema.
3.  Execute o arquivo `main.py` a partir do terminal:

    ```bash
    python main.py
    ```

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

*   **Cadastrar paciente:** Permite cadastrar um novo paciente, incluindo nome, telefone, email e CPF.
*   **Nova consulta:** Permite marcar uma nova consulta, selecionando o paciente, a data e hora da consulta, e a especialidade médica.
*   **Consultas agendadas:** Lista todas as consultas agendadas, mostrando o nome do paciente, a data e hora da consulta, e a especialidade médica.
*   **Cancelar consultas:** Permite cancelar uma consulta existente, selecionando o número da consulta na lista.
*   **Sair:** Encerra o programa.

## Arquivos

### `main.py`

Este arquivo contém o menu principal do sistema e a lógica para interagir com os outros módulos. Ele utiliza as funções definidas em `paciente.py` e `consulta.py` para realizar as operações.

### `paciente.py`

Este arquivo contém a função `addPaciente` que permite cadastrar um novo paciente. A função recebe os dados do paciente (nome, telefone, email e CPF) e os armazena em uma lista de pacientes.

### `consulta.py`

Este arquivo contém as funções relacionadas às consultas:

*   `marcarConsulta`: Permite marcar uma nova consulta, selecionando o paciente, a data e hora da consulta, e a especialidade médica.
*   `consultasAgendadas`: Lista todas as consultas agendadas.
*   `cancelarConsulta`: Permite cancelar uma consulta existente.

## Dependências

Este projeto não possui dependências externas além da biblioteca padrão do Python.

## Observações

Este é um sistema básico de agendamento de consultas. Melhorias podem ser feitas, como adicionar persistência de dados (salvar os dados em arquivos), validação de dados de entrada, interface gráfica, entre outros.
