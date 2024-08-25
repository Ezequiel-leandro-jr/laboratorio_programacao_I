from funcao_busca import funcao_busca
from funcao_exibir import funcao_exibir
from cabecalhos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar
import time

def deletar(portfolio, placa):
    while True:
        veiculo = funcao_busca(portfolio, placa)
        if veiculo:
            funcao_exibir(veiculo)
            n = '4'
            while n == '4':
                n = input('DELETAR [1]\nNOVA BUSCA [2]\nVOLTAR AO MENU [3]\n>>> ')
                match n:
                    case '1':
                        portfolio.remove(veiculo)
                        print('VEÍCULO DELETADO COM SUCESSO!')
                        time.sleep(2)
                        n = '0'
                        while n == '0':
                            n = input('DELETAR OUTRO VEÍCULO [1]\nVOLTAR AO MENU [2]')
                            if n == '1':
                                placa = input('PLACA: ')
                            elif n == '2':
                                return
                            else:
                                print('Erro: opção inválida!')
                                n = '0'
                                time.sleep(1)        
                    case '2':
                        placa = input('PLACA: ')
                        n = '5'
                    case '3':
                        n = '5'
                        return
                    case _:
                        print('ERRO: opção inválida!')
                        n = '4'
                        time.sleep(1)
        else:
            print('ERRO: Veículo não encontrado!')
            while True:
                n = input('NOVA DELEÇÃO [1]\nVOLTAR AO MENU [2]\n>> ')
                if n == '1':
                    placa = input('PLACA: ')
                    break  
                elif n == '2':
                    return 
                else:
                    print('ERRO: Opção inválida!')
                    time.sleep(1)        
            