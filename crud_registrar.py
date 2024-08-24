# placa, tipo, marca, modelo, cor, ano_fabricacao, portas, combustivel, conservacao, quilometragem, preco, status
import time
from classe_veiculo import Veiculo
from funcao_exibir import funcao_exibir

    
def cadastrar(portfolio):
    n = '0'
    while n == '0':
        tipo = '8'
        combustivel = '8'
        conservacao = '3'
        status = '5'
            
        placa = input('PLACA: ')
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
                    tipo = 'Camioneta'
                case '2':
                    tipo = 'Camionhonete'
                case '3':
                    tipo = 'Caminhao'
                case '4':
                    tipo = 'Carro'
                case '5':
                    tipo = 'Carreta'
                case '6':
                    tipo = 'Motocicleta'
                case '7':
                    tipo = 'Outro'
                case _:
                    print('ERRO: Opcao incorreta! Tente novamente!')
                    tipo = '8'
                    time.sleep(1)
            
        marca = input('MARCA: ')
        modelo = input('MODELO: ')
        cor = input('COR: ')
        ano_fabricacao = input('ANO: ')
        portas = int(input('PORTAS: '))
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
                    combustivel = 'Gasolina'
                case '2':
                    combustivel = 'GLP'
                case '3':
                    combustivel = 'Etanol'
                case '4':
                    combustivel = 'GNV'
                case '5':
                    combustivel = 'Eletrico'
                case '6':
                    combustivel = 'Hibrido'
                case '7':
                    combustivel = 'Outro'
                case _:
                    print('ERRO: Opcao incorreta! Tente novamente!')
                    combustivel = '8'
                    time.sleep(1) 
        while conservacao == '3':
            conservacao = input('ESTADO DE CONSERVACAO:\n1. Novo\n2. Seminovo\n----------------\nOP: ')
            match conservacao:
                case '1':
                    conservacao = 'Novo'
                case '2':
                    conservacao = 'Seminovo'
                case _:
                    print('ERRO: Opcao incorreta! Tente novamente!')
                    conservacao = '3'
                    time.sleep(1)     
        quilometragem = float(input('QUILOMETRAGEM (KM): '))
        preco = float(input('PRECO (R$): '))
        while status == '5':
            status = input('STATUS:\n1. A venda\n2. Reservado\n3. Vendido\n4. Indisponivel\n----------------\nOP: ')
            match status:
                case '1':
                    status = 'A venda'
                case '2':
                    status = 'Reservado'
                case '3':
                    status = 'Vendido'
                case '4':
                    status = 'Indisponivel'
                case _:
                    print('ERRO: Opcao incorreta! Tente novamente!')
                    status = '5'
                    time.sleep(1)              
        novo_veiculo = Veiculo(placa, tipo, marca, modelo, cor, ano_fabricacao, portas, combustivel, conservacao, quilometragem, preco, status)
        print('CADASTRO REALIZADO COM SUCESSO!')
        portfolio.append(novo_veiculo)
        funcao_exibir(novo_veiculo)
        
        n = '3'
        while n == '3':
            n = input('NOVO CADASTRO [1]\nVOLTAR AO MENU [2]\n>>> ')
            if n == '1':
                print('')
                n = '0'
            elif n == '2':
                print('')
            else:
                print('ERRO: opcao invalida!')
                n = '3'
                time.sleep(1)
    
