# placa, tipo, marca, modelo, cor, ano_fabricacao, portas, combustivel, conservacao, quilometragem, preco, status
import time
from classe_veiculo import Veiculo
from funcao_exibir import funcao_exibir
from crud_listar import listar
from cabecalhos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar
import os
    
def cadastrar(portfolio):
    n = '0'
    while n == '0':
        tipo = '8'
        combustivel = '8'
        conservacao = '3'
        status = '5'
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()    
        placa = input('PLACA: ')
        while tipo == '8':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_registrar()
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
            match tipo:
                case '1':
                    tipo = 'Camioneta'
                case '2':
                    tipo = 'Caminhonete'
                case '3':
                    tipo = 'Caminhão'
                case '4':
                    tipo = 'Carro'
                case '5':
                    tipo = 'Carreta'
                case '6':
                    tipo = 'Motocicleta'
                case '7':
                    tipo = 'Outro'
                case _:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_registrar()
                    print('ERRO: Opção inválida!')
                    tipo = '8'
                    time.sleep(1)
                    
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()   
        marca = input('MARCA: ')
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()
        modelo = input('MODELO: ')
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()
        cor = input('COR: ')
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()
        ano_fabricacao = input('ANO: ')
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()
        portas = int(input('PORTAS: '))
        while combustivel == '8':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_registrar()
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
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_registrar()
                    print('ERRO: Opcao incorreta! Tente novamente!')
                    combustivel = '8'
                    time.sleep(1) 
        while conservacao == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_registrar()
            conservacao = input('ESTADO DE CONSERVACAO:\n1. Novo\n2. Seminovo\n----------------\nOP: ')
            match conservacao:
                case '1':
                    conservacao = 'Novo'
                case '2':
                    conservacao = 'Seminovo'
                case _:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_registrar()
                    print('ERRO: Opcao incorreta! Tente novamente!')
                    conservacao = '3'
                    time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()     
        quilometragem = float(input('QUILOMETRAGEM (KM): '))
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_registrar()
        preco = float(input('PREÇO (R$): '))
        while status == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_registrar()
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
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_registrar()
                    print('ERRO: Opcao incorreta! Tente novamente!')
                    status = '5'
                    time.sleep(1)              
        novo_veiculo = Veiculo(placa, tipo, marca, modelo, cor, ano_fabricacao, portas, combustivel, conservacao, quilometragem, preco, status)
        portfolio.append(novo_veiculo)
        
        
        n = '3'
        while n == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_registrar()
            print('REGISTRO REALIZADO COM SUCESSO!')
            funcao_exibir(novo_veiculo)
            n = input('NOVO REGISTRO [1]\nLISTAR VEÍCULOS [2]\nVOLTAR AO MENU [3]\n>>> ')
            if n == '1':
                n = '0'
            elif n == '2':
                listar(portfolio)
                return
            elif n == '3':
                return
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                titulo_automarket()
                titulo_registrar()
                print('ERRO: opção inválida!')
                n = '3'
                time.sleep(1)
    
