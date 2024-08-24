from funcao_busca import funcao_busca
from funcao_exibir import funcao_exibir
import time

def deletar(portfolio):
    while True:
        veiculo = funcao_busca(portfolio)
        if veiculo:
            funcao_exibir(veiculo)
            n = '4'
            while n == '4':
                n = input('EXCLUIR [1]\nNOVA BUSCA [2]\nVOLTAR AO MENU [3]\n>>> ')
                match n:
                    case '1':
                        portfolio.remove(veiculo)
                        print('REGISTRO REMOVIDO COM SUCESSO!')
                        time.sleep(2)
                        n = '0'
                        while n == '0':
                            n = input('DELETAR OUTRO REGISTRO [1]\nVOLTAR AO MENU [2]')
                            if n == '1':
                                print('')
                            elif n == '2':
                                break
                            else:
                                print('Erro: opcao invalida!')
                                time.sleep(1)        
                    case '2':
                        print('')
                        n = '5'
                    case '3':
                        n = '5'
                        break
                    case _:
                        print('ERRO: opcao invalida!')
                        n = '4'
                        time.sleep(1)
                
            