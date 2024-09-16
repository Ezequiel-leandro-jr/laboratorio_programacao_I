##Arquivo cabecalhos.py##
'''
Todas as funções abaixo fazem parte do arquivo 
'''

def titulo_automarket():
    print('''
  ===|| AUTOMARKET ||===

''')

def titulo_buscar():
    print('''
      BUSCAR VEÍCULO
--------------------------
''')

def titulo_deletar():
    print('''
      DELETAR VEÍCULO
--------------------------
''')

def titulo_editar():
    print('''
      EDITAR VEÍCULO
--------------------------
''')

def titulo_listar():
    print('''
      LISTAGEM GERAL
--------------------------
''')

def titulo_registrar():
    print('''
    REGISTRAR VEÍCULO
--------------------------
''')


## Arquivo classe_veiculo.py ##
'''
classe presente no arquivo
'''

class Veiculo:
    def __init__(self, placa, tipo, marca, modelo, cor, ano_fabricacao, portas, combustivel, conservacao, quilometragem, preco, status):
        self.placa = placa
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano_fabricacao = ano_fabricacao
        self.portas = portas
        self.combustivel = combustivel
        self.conservacao = conservacao
        self.quilometragem = quilometragem
        self.preco = preco
        self.status = status
        

## Arquivo funcao_busca.py ##
def funcao_busca(portfolio, placa):
    if placa:
        for veiculo in portfolio:
            if veiculo.placa == placa:
                return veiculo
    else:
        return
    

## Arquivo funcao_exibir.py ##
def funcao_exibir(veiculo):
    print(f'''
VEÍCULO:
----------------------------------------------------------------------------------------------------------------------
PLACA: {veiculo.placa} | TIPO: {veiculo.tipo} | MARCA: {veiculo.marca} | MODELO: {veiculo.modelo}
ANO: {veiculo.ano_fabricacao} | COR: {veiculo.cor} | PORTAS: {veiculo.portas} | COMBUSTÍVEL: {veiculo.combustivel}
ESTADO: {veiculo.conservacao} | QUILOMETRAGEM: {veiculo.quilometragem:.2f}Km | PREÇO: R${veiculo.preco:.2f}
STATUS: {veiculo.status}
______________________________________________________________________________________________________________________

''')


## Arquivo funcao_placa.py ##
def funcao_placa(portfolio, placa):
    if not placa:  # Se a placa não for fornecida
        placa = input("Digite a placa do veículo: ")
    return placa


## Arquivo persistencia.py ##
import pandas as pd
import os
from classe_veiculo import Veiculo

def cria_banco():
    file = 'banco.xlsx'

    if os.path.exists(file):
        dfbanco = pd.read_excel(file, dtype={
            'placa': str,
            'tipo': str,
            'marca': str,
            'modelo': str,
            'cor': str,
            'ano_fabricacao': str,
            'portas': int,  
            'combustivel': str,
            'conservacao': str,
            'quilometragem': float,  
            'preco': float,  
            'status': str })
        dfdict = dfbanco.to_dict(orient='records')
        lista_de_objetos = [Veiculo(**dados) for dados in dfdict]
        return lista_de_objetos
    else:
        return []  


def salva_banco(portfolio):
    file = 'banco.xlsx'
    
    lista_dicts = [{
        'placa': str(veiculo.placa),
        'tipo': str(veiculo.tipo),
        'marca': str(veiculo.marca),
        'modelo': str(veiculo.modelo),
        'cor': str(veiculo.cor),
        'ano_fabricacao': str(veiculo.ano_fabricacao),
        'portas': veiculo.portas,
        'combustivel': str(veiculo.combustivel),
        'conservacao': str(veiculo.conservacao),
        'quilometragem': veiculo.quilometragem,
        'preco': veiculo.preco,
        'status': str(veiculo.status)
        
    } for veiculo in portfolio]

    df = pd.DataFrame(lista_dicts)
    df.to_excel(file, index=False)


## Arquivo Main.py ##
from classe_veiculo import Veiculo
from persistencia import cria_banco, salva_banco
from crud_registrar import cadastrar
from crud_editar import editar
from crud_buscar import buscar
from crud_listar import listar
from crud_deletar import deletar
from cabecalhos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar, titulo_listar
import time
import os

portfolio = cria_banco()
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    titulo_automarket()
    op = input('''
         MENU
---------------------
1. REGISTRAR VEICULO
2. BUSCAR VEICULO
3. EDITAR VEICULO
4. LISTAR PORTFOLIO
5. DELETAR VEICULO

0. SAIR DO SISTEMA
---------------------
OP: ''')

    match op:
        case '1':
            cadastrar(portfolio)
            salva_banco(portfolio)
        case '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_buscar()
            buscar(portfolio, placa)
            salva_banco(portfolio)
        case '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_editar()
            editar(portfolio, placa)
            salva_banco(portfolio)
        case '4':
            listar(portfolio)
            salva_banco(portfolio)
        case '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_deletar()
            deletar(portfolio, placa)
            salva_banco(portfolio)
        case '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            print('\nSAINDO DO SISTEMA...')
            time.sleep(1)
            salva_banco(portfolio)
            break
        case _:
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            print('\nERRO: OPCAO INVALIDA!')
            salva_banco(portfolio)
            time.sleep(1)


## Arquivo crud_buscar.py ##
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
                    
                    
## Arquivo crud_deletar.py ##
from funcao_busca import funcao_busca
from funcao_placa import funcao_placa
from funcao_exibir import funcao_exibir
from cabecalhos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar
import time
import os

def deletar(portfolio, placa):
    placa = funcao_placa(portfolio, placa)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_deletar()
        veiculo = funcao_busca(portfolio, placa)
        if veiculo:
            n = '4'
            while n == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                titulo_automarket()
                titulo_deletar()
                funcao_exibir(veiculo)
                n = input('DELETAR [1]\nNOVA BUSCA [2]\nVOLTAR AO MENU [3]\n>>> ')
                match n:
                    case '1':
                        portfolio.remove(veiculo)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        titulo_automarket()
                        titulo_deletar()
                        print('VEÍCULO DELETADO COM SUCESSO!')
                        time.sleep(2)
                        n = '0'
                        while n == '0':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            titulo_automarket()
                            titulo_deletar()
                            n = input('DELETAR OUTRO VEÍCULO [1]\nVOLTAR AO MENU [2]\n>>> ')
                            if n == '1':
                                os.system('cls' if os.name == 'nt' else 'clear')
                                titulo_automarket()
                                titulo_deletar()
                                placa = funcao_placa(portfolio, placa)
                            elif n == '2':
                                return
                            else:
                                print('\nERRO: opção inválida!')
                                n = '0'
                                time.sleep(1)        
                    case '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        titulo_automarket()
                        titulo_deletar()
                        placa = funcao_placa(portfolio, placa)
                        n = '5'
                    case '3':
                        n = '5'
                        return
                    case _:
                        print('\nERRO: opção inválida!')
                        n = '4'
                        time.sleep(1)
        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                titulo_automarket()
                titulo_deletar()
                print('\nERRO: Veículo não encontrado!')
                n = input('NOVA DELEÇÃO [1]\nVOLTAR AO MENU [2]\n>> ')
                if n == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    titulo_automarket()
                    titulo_deletar()
                    placa = funcao_placa(portfolio, placa)
                    break  
                elif n == '2':
                    return 
                else:
                    print('\nERRO: Opção inválida!')
                    time.sleep(1)        
            

## Arquivo crud_editar.py ##
from funcao_busca import funcao_busca
from funcao_placa import funcao_placa
from classe_veiculo import Veiculo
from funcao_exibir import funcao_exibir
from cabecalhos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar
import time
import os

def editar(portfolio, placa):
    placa = funcao_placa(portfolio, placa)
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
                            veiculo.placa = input('PLACA: ').strip()
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


## Arquivo crud_registrar.py ##
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
        placa = input('PLACA: ').strip()
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
    

## Arquivo crud_listar.py ##
from crud_editar import editar
from funcao_placa import funcao_placa
from crud_deletar import deletar
from cabecalhos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar, titulo_listar
import time
import os


def listar(portfolio):
    while True:
        i = 1
        soma = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo_automarket()
        titulo_listar()
        for veiculo in portfolio:
            print(f'''
    VEíCULO {i}:
    ----------------------------------------------------------------------------------------------------------------------
    PLACA: {veiculo.placa} | TIPO: {veiculo.tipo} | MARCA: {veiculo.marca} | MODELO: {veiculo.modelo}
    ANO: {veiculo.ano_fabricacao} | COR: {veiculo.cor} | PORTAS: {veiculo.portas} | COMBUSTÍVEL: {veiculo.combustivel}
    ESTADO: {veiculo.conservacao} | QUILOMETRAGEM: {veiculo.quilometragem:.2f}Km | PREÇO: R${veiculo.preco:.2f}
    STATUS: {veiculo.status}
    ----------------------------------------------------------------------------------------------------------------------
    ''')
            i += 1
            soma += 1
            
        print(f'\nTOTAL DE VEÍCULOS: {soma}\n ______________________________________________________________________________________________________________________')
            
        n = input('\nEDITAR VEÍCULO [1]\nDELETAR VEÍCULO [2]\nVOLTAR AO MENU [3]\n>>> ')
        if n == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_listar()
            placa = funcao_placa(portfolio, placa)
            editar(portfolio, placa)
            return
        elif n == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo_automarket()
            titulo_listar()
            placa = funcao_placa(portfolio, placa)
            deletar(portfolio, placa)
            return
                
        elif n == '3':
            return
        else:
            print('\nERRO: opção inválida!')
            time.sleep(1)





