from funcao_busca import funcao_busca
from classe_veiculo import Veiculo
from funcao_exibir import funcao_exibir
import time

def editar(portfolio, placa):
    while True:
        veiculo = funcao_busca(portfolio, placa)
        
        if veiculo:
            indice = portfolio.index(veiculo)
            while True:
                print('DESEJA ALTERAR O VEICULO ABAIXO?')
                funcao_exibir(veiculo)
                op = input('1. Sim   2. Não\n>> ') 
                if op == '1':
                    while True:
                        funcao_exibir(veiculo)
                        alterar = input('SELECIONE O CAMPO:\n1. Placa\n2. Tipo\n3. Marca\n4. Modelo\n5. Cor\n6. Ano de fabricação\n7. Portas\n8. Combustível\n9. Conservação\n10. Quilometragem\n11. Preço\n12. Status\n>> ')
                        if alterar == '1':
                            veiculo.placa = input('PLACA: ')
                        elif alterar == '2':
                            while True:
                                tipo = input('''
TIPO:
1. Camioneta
2. Caminhonete
3. Caminhão
4. Carro
5. Carreta
6. Motocicleta
7. Outro
----------------
OP: ''')
                                if tipo in ['1', '2', '3', '4', '5', '6', '7']:
                                    tipos = ['Camioneta', 'Caminhonete', 'Caminhão', 'Carro', 'Carreta', 'Motocicleta', 'Outro']
                                    veiculo.tipo = tipos[int(tipo) - 1]
                                    break
                                else:
                                    print('ERRO: Opção incorreta! Tente novamente!')
                                    time.sleep(1)
                        elif alterar == '3':
                            veiculo.marca = input('MARCA: ')
                        elif alterar == '4':
                            veiculo.modelo = input('MODELO: ')
                        elif alterar == '5':
                            veiculo.cor = input('COR: ')
                        elif alterar == '6':
                            veiculo.ano_fabricacao = input('ANO: ')
                        elif alterar == '7':
                            veiculo.portas = int(input('PORTAS: '))
                        elif alterar == '8':
                            while True:
                                combustivel = input('''
COMBUSTÍVEL:
1. Gasolina
2. GLP
3. Etanol
4. GNV
5. Elétrico
6. Híbrido
7. Outro
----------------
OP: ''')
                                if combustivel in ['1', '2', '3', '4', '5', '6', '7']:
                                    combustiveis = ['Gasolina', 'GLP', 'Etanol', 'GNV', 'Elétrico', 'Híbrido', 'Outro']
                                    veiculo.combustivel = combustiveis[int(combustivel) - 1]
                                    break
                                else:
                                    print('ERRO: Opção incorreta! Tente novamente!')
                                    time.sleep(1)
                        elif alterar == '9':
                            while True:
                                conservacao = input('ESTADO DE CONSERVAÇÃO:\n1. Novo\n2. Seminovo\n----------------\nOP: ')
                                if conservacao in ['1', '2']:
                                    veiculo.conservacao = 'Novo' if conservacao == '1' else 'Seminovo'
                                    break
                                else:
                                    print('ERRO: Opção incorreta! Tente novamente!')
                                    time.sleep(1)
                        elif alterar == '10':
                            veiculo.quilometragem = float(input('QUILOMETRAGEM (KM): '))
                        elif alterar == '11':
                            veiculo.preco = float(input('PREÇO (R$): '))
                        elif alterar == '12':
                            while True:
                                status = input('STATUS:\n1. À venda\n2. Reservado\n3. Vendido\n4. Indisponível\n----------------\nOP: ')
                                if status in ['1', '2', '3', '4']:
                                    status_opcoes = ['À venda', 'Reservado', 'Vendido', 'Indisponível']
                                    veiculo.status = status_opcoes[int(status) - 1]
                                    break
                                else:
                                    print('ERRO: Opção incorreta! Tente novamente!')
                                    time.sleep(1)
                        else:
                            print('ERRO: Opção incorreta! Tente novamente!')
                            time.sleep(1)
                            continue

                        portfolio[indice] = veiculo

                        n = input('EDIÇÃO REALIZADA COM SUCESSO!\nEDITAR OUTRO CAMPO [1]\nEDITAR NOVO VEICULO [2]\nVOLTAR AO MENU [3]\n>> ')
                        if n == '1':
                            continue
                        elif n == '2':
                            placa = input('PLACA: ')
                            break  
                        elif n == '3':
                            return 
                        else:
                            print('ERRO: opção inválida!')
                            time.sleep(1)
                elif op == '2':
                    while True:
                        n = input('EDITAR NOVO VEICULO [1]\nVOLTAR AO MENU [2]\n>> ')
                        if n == '1':
                            placa = input('PLACA: ')
                            break
                        elif n == '2':
                            return  
                        else:
                            print('ERRO: Opção inválida!')
                            time.sleep(1)
                    break
                else:
                    print('ERRO: Opção inválida!')
                    time.sleep(1)
        else:
            print('ERRO: Veículo não encontrado!')
            while True:
                n = input('EDITAR NOVO VEICULO [1]\nVOLTAR AO MENU [2]\n>> ')
                if n == '1':
                    placa = input('PLACA: ')
                    break  
                elif n == '2':
                    return 
                else:
                    print('ERRO: Opção inválida!')
                    time.sleep(1)
