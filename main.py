from classe_veiculo import Veiculo
from persistencia import cria_banco, salva_banco
from crud_registrar import cadastrar
from crud_editar import editar
from crud_buscar import buscar
from crud_listar import listar
from crud_deletar import deletar
from cabecalhos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar, titulo_listar
import time
import os

portfolio = cria_banco()
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
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
            salva_banco(portfolio)
        case '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_buscar()
            placa = input('PLACA: ').strip()
            buscar(portfolio, placa)
            salva_banco(portfolio)
        case '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_editar()
            placa = input('PLACA: ').strip()
            editar(portfolio, placa)
            salva_banco(portfolio)
        case '4':
            listar(portfolio)
            salva_banco(portfolio)
        case '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_deletar()
            placa = input('PLACA: ').strip()
            deletar(portfolio, placa)
            salva_banco(portfolio)
        case '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            print('\nSAINDO DO SISTEMA...')
            time.sleep(1)
            salva_banco(portfolio)
            break
        case _:
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            print('\nERRO: OPCAO INVALIDA!')
            salva_banco(portfolio)
            time.sleep(1)
