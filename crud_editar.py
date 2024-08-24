# placa, tipo, marca, modelo, cor, ano_fabricacao, portas, combustivel, conservacao, quilometragem, preco, status
from funcao_busca import funcao_busca
from classe_veiculo import Veiculo
from funcao_exibir import funcao_exibir
import time

def editar(portfolio):
    while True:
        veiculo = funcao_busca(portfolio)
        indice = portfolio.index(veiculo)
        
        if veiculo:
            op = '3'
            while op == '3':
                print('DESEJA ALTERAR O VEICULO ABAIXO?')
                funcao_exibir(veiculo)
                op = input('1. Sim   2. Nao\n>> ')
                if op == '1':
                    opcao = '13'
                    while opcao == '13':
                        funcao_exibir(veiculo)
                        opcao = input('SELECIONE O CAMPO:\n1. Placa\n2. Tipo\n3. Marca\n4. Modelo\n5. Cor\n6. Ano de fabricacao\n7. Portas\n8. Combustivel\n9. Conservacao\n10. Quilometragem\n11. Preco\n12. Status')
                        match opcao:
                            case '1':
                                placa = input('PLACA: ')
                                veiculo.placa = placa
                                portfolio[indice] = veiculo
                            case '2':
                                while tipo == '8':
                                    tipo = input('''
    TIPO:
    1. Camioneta
    2. Caminhonete
    3. Caminhao
    4. Carro
    5. Carreta
    6. Motocicleta
    7. Outro
    ----------------
    OP: ''')
                                    match tipo:
                                        case '1':
                                            veiculo.tipo = 'Camioneta'
                                        case '2':
                                            veiculo.tipo = 'Camionhonete'
                                        case '3':
                                            veiculo.tipo = 'Caminhao'
                                        case '4':
                                            veiculo.tipo = 'Carro'
                                        case '5':
                                            veiculo.tipo = 'Carreta'
                                        case '6':
                                            veiculo.tipo = 'Motocicleta'
                                        case '7':
                                            veiculo.tipo = 'Outro'
                                        case _:
                                            print('ERRO: Opcao incorreta! Tente novamente!')
                                            tipo = '8'
                                            time.sleep(1)            
                                portfolio[indice] = veiculo                          
                            case '3':
                                marca = input('MARCA: ')
                                veiculo.marca = marca
                                portfolio[indice] = veiculo   
                            case '4':
                                modelo = input('MODELO: ')
                                veiculo.modelo = modelo
                                portfolio[indice] = veiculo
                            case '5':
                                cor = input('COR: ')
                                veiculo.cor = cor
                                portfolio[indice] = veiculo
                            case '6':
                                ano_fabricacao = input('ANO: ')
                                veiculo.ano_fabricacao = ano_fabricacao
                                portfolio[indice] = veiculo
                            case '7':
                                portas = int(input('PORTAS: '))
                                veiculo.portas = portas
                                portfolio[indice] = veiculo
                            case '8':
                                combustivel = '8'
                                while combustivel == '8':
                                    combustivel = input('''
TIPO:
1. Gasolina
2. GLP
3. Etanol
4. GNV
5. Eletrico
6. Hibrido
7. Outro
----------------
OP: ''')
                                    match combustivel:
                                        case '1':
                                            veiculo.combustivel = 'Gasolina'
                                        case '2':
                                            veiculo.combustivel = 'GLP'
                                        case '3':
                                            veiculo.combustivel = 'Etanol'
                                        case '4':
                                            veiculo.combustivel = 'GNV'
                                        case '5':
                                            veiculo.combustivel = 'Eletrico'
                                        case '6':
                                            veiculo.combustivel = 'Hibrido'
                                        case '7':
                                            veiculo.combustivel = 'Outro'
                                        case _:
                                            print('ERRO: Opcao incorreta! Tente novamente!')
                                            combustivel = '8'
                                            time.sleep(1)
                                portfolio[indice] = veiculo
                            case '9':
                                conservacao = '3'
                                while conservacao == '3':
                                    conservacao = input('ESTADO DE CONSERVACAO:\n1. Novo\n2. Seminovo\n----------------\nOP: ')
                                    match conservacao:
                                        case '1':
                                            veiculo.conservacao = 'Novo'
                                        case '2':
                                            veiculo.conservacao = 'Seminovo'
                                        case _:
                                            print('ERRO: Opcao incorreta! Tente novamente!')
                                            conservacao = '3'
                                            time.sleep(1)
                                portfolio[indice] = veiculo
                            case '10':
                                quilometragem = float(input('QUILOMETRAGEM (KM): '))
                                veiculo.quilometragem = quilometragem
                                portfolio[indice] = veiculo
                            case '11':
                                preco = float(input('PRECO (R$): '))
                                veiculo.preco = preco
                                portfolio[indice] = veiculo
                            case '12':
                                status = '5'
                                while status == '5':
                                    status = input('STATUS:\n1. A venda\n2. Reservado\n3. Vendido\n4. Indisponivel\n----------------\nOP: ')
                                    match status:
                                        case '1':
                                            veiculo.status = 'A venda'
                                        case '2':
                                            veiculo.status = 'Reservado'
                                        case '3':
                                            veiculo.status = 'Vendido'
                                        case '4':
                                            veiculo.status = 'Indisponivel'
                                        case _:
                                            print('ERRO: Opcao incorreta! Tente novamente!')
                                            status = '5'
                                            time.sleep(1)
                                portfolio[indice] = veiculo
                            case _:
                                print('ERRO: Opcao incorreta! Tente novamente!')
                                opcao == '13'
                                time.sleep(1)
                        n = 4    
                        while n == '4':
                            print('EDICAO REALIZADA COM SUCESSO!')
                            funcao_exibir(veiculo)
                            n = input('EDITAR OUTRO CAMPO [1]\nEDITAR NOVO VEICULO [2]\nVOLTAR AO MENU [3]')
                            if n == '1':
                                opcao = '13'
                            elif n == '2':
                                 op = '4'
                                 opcao = '14'
                            elif n == '3':
                                break
                            else:
                                print('ERRO: opcao invalida!')
                                n = '4'
                                time.sleep(1) 
        else:
            print('ERRO: veiculo nao encontrado! Tente novamente.')
            time.sleep(2)
                
            
        