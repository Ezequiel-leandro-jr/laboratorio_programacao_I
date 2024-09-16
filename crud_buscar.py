from funcao_busca import funcao_busca
from funcao_exibir import funcao_exibir
from funcao_placa import funcao_placa
from crud_editar import editar
from crud_deletar import deletar
from cabecalhos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar
import time
import os

def buscar(portfolio, placa):
    placa = funcao_placa(portfolio, placa)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_buscar()
        veiculo = funcao_busca(portfolio, placa)
        if veiculo:
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_buscar()
            funcao_exibir(veiculo)
            op = input('EDITAR [1]\nDELETAR [2]\nNOVA BUSCA [3]\nVOLTAR AO MENU [4]\n>>> ')
            match op:
                case '1':
                    editar(portfolio, placa)
                    break
                case '2':
                    deletar(portfolio, placa)
                    break
                case '3':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_buscar()
                    placa = funcao_placa(portfolio, placa)
                    continue
                case '4':
                    return
                case _:
                    print('\nERRO: opção inválida!')
                    time.sleep(1)
        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                titulo_automarket()
                titulo_buscar()
                print('ERRO: Veículo não encontrado!')
                n = input('NOVA BUSCA [1]\nVOLTAR AO MENU [2]\n>> ')
                if n == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_buscar()
                    placa = funcao_placa(portfolio, placa)
                    break  
                elif n == '2':
                    return 
                else:
                    print('\nERRO: Opção inválida!')
                    time.sleep(1)