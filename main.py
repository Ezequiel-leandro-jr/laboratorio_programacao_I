from classe_veiculo import Veiculo
from crud_registrar import cadastrar
from crud_editar import editar
from crud_buscar import buscar
from crud_listar import listar
from crud_deletar import deletar
from cabecalhos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar
import time
import os

portfolio = []
while True:
    titulo_automarket()
    op = input('''
         MENU
---------------------
1. REGISTRAR VEICULO
2. BUSCAR VEICULO
3. EDITAR VEICULO
4. LISTAR PORTFOLIO
5. DELETAR VEICULO

0. SAIR DO SISTEMA
---------------------
OP: ''')

    match op:
        case '1':
            cadastrar(portfolio)
        case '2':
            placa = input('PLACA: ')
            buscar(portfolio, placa)
        case '3':
            placa = input('PLACA: ')
            editar(portfolio, placa)
        case '4':
            listar(portfolio)
        case '5':
            placa = input('PLACA: ')
            deletar(portfolio, placa)
        case '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            print('\nSAINDO DO SISTEMA...')
            time.sleep(1)
            break
        case _:
            print('ERRO: OPCAO INVALIDA!')
            time.sleep(1)