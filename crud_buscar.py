from funcao_busca import funcao_busca
from funcao_exibir import funcao_exibir
from crud_editar import editar
import time

def buscar(portfolio):
    veiculo = funcao_busca(portfolio)
    
    while True:
        if veiculo:
            funcao_exibir(veiculo)
            op = input('EDITAR [1]\nEXCLUIR [2]\nNOVA BUSCA [3]\nVOLTAR AO MENU [4]\n>>> ')
            match op:
                case '1':
                    editar(portfolio)
                    break
                case '2':
                    excluir(portfolio)
                    break
                case '3':
                    break
                case _:
                    print('ERRO: opcao invalida!')
                    time.sleep(1)
        