from funcao_busca import funcao_busca
from classe_veiculo import Veiculo
from funcao_exibir import funcao_exibir
from cabecalhos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar
import time
import os

def editar(portfolio, placa):
    while True:
        veiculo = funcao_busca(portfolio, placa)

        if veiculo:
            indice = portfolio.index(veiculo)
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                titulo_automarket()
                titulo_editar()
                funcao_exibir(veiculo)
                op = input('CONTINUAR EDIÇÃO [1]\nEDITAR OUTRO VEÍCULO [2]\nVOLTAR AO MENU [3]\n>>> ') 
                if op == '1':
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        titulo_automarket()
                        titulo_editar()
                        funcao_exibir(veiculo)
                        alterar = input('SELECIONE O CAMPO:\n1. Placa\n2. Tipo\n3. Marca\n4. Modelo\n5. Cor\n6. Ano de fabricação\n7. Portas\n8. Combustível\n9. Conservação\n10. Quilometragem\n11. Preço\n12. Status\n\n0. Voltar\n>> ')
                        if alterar == '1':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            veiculo.placa = input('PLACA: ')
                            portfolio[indice] = veiculo
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '2':
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                titulo_automarket()
                                titulo_editar()
                                tipo = input('''
TIPO:
1. Camioneta
2. Caminhonete
3. Caminhão
4. Carro
5. Carreta
6. Motocicleta
7. Outro

0. Voltar
----------------
OP: ''')
                                if tipo in ['1', '2', '3', '4', '5', '6', '7']:
                                    tipos = ['Camioneta', 'Caminhonete', 'Caminhão', 'Carro', 'Carreta', 'Motocicleta', 'Outro']
                                    veiculo.tipo = tipos[int(tipo) - 1]
                                    portfolio[indice] = veiculo
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                                    time.sleep(2)
                                    break
                                elif tipo == '0':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('EDIÇÃO CANCELADA!')
                                    time.sleep(2)
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('\nERRO: Opção incorreta! Tente novamente!')
                                    time.sleep(1)
                        elif alterar == '3':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            veiculo.marca = input('MARCA: ')
                            portfolio[indice] = veiculo
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '4':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            veiculo.modelo = input('MODELO: ')
                            portfolio[indice] = veiculo
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '5':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            veiculo.cor = input('COR: ')
                            portfolio[indice] = veiculo
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '6':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            veiculo.ano_fabricacao = input('ANO: ')
                            portfolio[indice] = veiculo
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '7':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            veiculo.portas = int(input('PORTAS: '))
                            portfolio[indice] = veiculo
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '8':
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                titulo_automarket()
                                titulo_editar()
                                combustivel = input('''
COMBUSTÍVEL:
1. Gasolina
2. GLP
3. Etanol
4. GNV
5. Elétrico
6. Híbrido
7. Outro

0. Voltar
----------------
OP: ''')
                                if combustivel in ['1', '2', '3', '4', '5', '6', '7']:
                                    combustiveis = ['Gasolina', 'GLP', 'Etanol', 'GNV', 'Elétrico', 'Híbrido', 'Outro']
                                    veiculo.combustivel = combustiveis[int(combustivel) - 1]
                                    portfolio[indice] = veiculo
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                                    time.sleep(2)
                                    break
                                elif combustivel == '0':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('EDIÇÃO CANCELADA!')
                                    time.sleep(2)
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('ERRO: Opção incorreta! Tente novamente!')
                                    time.sleep(1)
                        elif alterar == '9':
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                titulo_automarket()
                                titulo_editar()
                                conservacao = input('ESTADO DE CONSERVAÇÃO:\n1. Novo\n2. Seminovo\n\n\n0. Voltar\n----------------\nOP: ')
                                if conservacao in ['1', '2']:
                                    veiculo.conservacao = 'Novo' if conservacao == '1' else 'Seminovo'
                                    portfolio[indice] = veiculo
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                                    time.sleep(2)
                                    break
                                elif conservacao == '0':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('EDIÇÃO CANCELADA!')
                                    time.sleep(2)
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('ERRO: Opção incorreta! Tente novamente!')
                                    time.sleep(1)
                        elif alterar == '10':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            veiculo.quilometragem = float(input('QUILOMETRAGEM (KM): '))
                            portfolio[indice] = veiculo
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '11':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            veiculo.preco = float(input('PREÇO (R$): '))
                            portfolio[indice] = veiculo
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                            time.sleep(2)
                        elif alterar == '12':
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                titulo_automarket()
                                titulo_editar()
                                status = input('STATUS:\n1. À venda\n2. Reservado\n3. Vendido\n4. Indisponível\n\n0. Voltar\n----------------\nOP: ')
                                if status in ['1', '2', '3', '4']:
                                    status_opcoes = ['À venda', 'Reservado', 'Vendido', 'Indisponível']
                                    veiculo.status = status_opcoes[int(status) - 1]
                                    portfolio[indice] = veiculo
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('\nEDIÇÃO REALIZADA COM SUCESSO!')
                                    time.sleep(2)
                                    break
                                elif status == '0':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('EDIÇÃO CANCELADA!')
                                    time.sleep(2)
                                    break
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    titulo_automarket()
                                    titulo_editar()
                                    print('ERRO: Opção inválida!')
                                    time.sleep(1)
                        elif alterar == '0':
                            break
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_editar()
                            print('ERRO: Opção inválida!')
                            time.sleep(1)
                            continue           
                            
                elif op == '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_editar()
                    placa = input('PLACA: ')
                    break
                elif op == '3':
                    return  
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_editar()
                    print('ERRO: Opção inválida!')
                    time.sleep(1)
        else:
            
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                titulo_automarket()
                titulo_editar()
                print('ERRO: Veículo não encontrado!')
                n = input('EDITAR NOVO VEÍCULO [1]\nVOLTAR AO MENU [2]\n>> ')
                if n == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_editar()
                    placa = input('PLACA: ')
                    break  
                elif n == '2':
                    return 
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_editar()
                    print('ERRO: Opção inválida!')
                    time.sleep(1)
