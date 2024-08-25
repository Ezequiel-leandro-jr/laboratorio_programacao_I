from crud_editar import editar
from crud_deletar import deletar
import time

def listar(portfolio):
    while True:
        i = 1
        soma = 0
        
        for veiculo in portfolio:
            print(f'''
    VEICULO {i}:
    ----------------------------------------------------------------------------------------------------------------------
    PLACA: {veiculo.placa} | TIPO: {veiculo.tipo} | MARCA: {veiculo.marca} | MODELO: {veiculo.modelo}
    ANO: {veiculo.ano_fabricacao} | COR: {veiculo.cor} | PORTAS: {veiculo.portas} | COMBUSTIVEL: {veiculo.combustivel}
    ESTADO: {veiculo.conservacao} | QUILOMETRAGEM: {veiculo.quilometragem:.2f}Km | PRECO: R${veiculo.preco:.2f}
    STATUS: {veiculo.status}
    ''')
            i += 1
            soma += 1
            
        print(f'TOTAL DE VEICULOS: {soma}\n______________________________________________________________________________________________________________________')
        while True:
            n = input('\nEDITAR VEICULO [1]\nDELETAR VEICULO [2]\nVOLTAR AO MENU [3]\n>>> ')
            if n == '1':
                placa = input('PLACA: ')
                editar(portfolio, placa)
                return
            elif n == '2':
                placa = input('PLACA: ')
                deletar(portfolio, placa)
                return
                
            elif n == '3':
                return
            else:
                print('ERRO: opcao invalida!')
                time.sleep(1)
