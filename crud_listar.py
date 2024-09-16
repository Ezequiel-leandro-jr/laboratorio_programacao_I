from crud_editar import editar
from funcao_placa import funcao_placa
from crud_deletar import deletar
from cabecalhos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar, titulo_listar
import time
import os


def listar(portfolio):
    while True:
        i = 1
        soma = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_listar()
        for veiculo in portfolio:
            print(f'''
    VEíCULO {i}:
    ----------------------------------------------------------------------------------------------------------------------
    PLACA: {veiculo.placa} | TIPO: {veiculo.tipo} | MARCA: {veiculo.marca} | MODELO: {veiculo.modelo}
    ANO: {veiculo.ano_fabricacao} | COR: {veiculo.cor} | PORTAS: {veiculo.portas} | COMBUSTÍVEL: {veiculo.combustivel}
    ESTADO: {veiculo.conservacao} | QUILOMETRAGEM: {veiculo.quilometragem:.2f}Km | PREÇO: R${veiculo.preco:.2f}
    STATUS: {veiculo.status}
    ----------------------------------------------------------------------------------------------------------------------
    ''')
            i += 1
            soma += 1
            
        print(f'\nTOTAL DE VEÍCULOS: {soma}\n ______________________________________________________________________________________________________________________')
            
        n = input('\nEDITAR VEÍCULO [1]\nDELETAR VEÍCULO [2]\nVOLTAR AO MENU [3]\n>>> ')
        if n == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_listar()
            placa = funcao_placa(portfolio, placa)
            editar(portfolio, placa)
            return
        elif n == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_listar()
            placa = funcao_placa(portfolio, placa)
            deletar(portfolio, placa)
            return
                
        elif n == '3':
            return
        else:
            print('\nERRO: opção inválida!')
            time.sleep(1)
