from funcao_busca import funcao_busca
from funcao_exibir import funcao_exibir
from crud_editar import editar
from crud_deletar import deletar
import time

def buscar(portfolio, placa):
    veiculo = funcao_busca(portfolio, placa)
    
    while True:
        if veiculo:
            funcao_exibir(veiculo)
            op = input('EDITAR [1]\nEXCLUIR [2]\nNOVA BUSCA [3]\nVOLTAR AO MENU [4]\n>>> ')
            match op:
                case '1':
                    editar(portfolio, placa)
                    break
                case '2':
                    deletar(portfolio, placa)
                    break
                case '3':
                    break
                case _:
                    print('ERRO: opcao invalida!')
                    time.sleep(1)
        