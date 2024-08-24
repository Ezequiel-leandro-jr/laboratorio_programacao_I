import time

def listar(portfolio):
    while True:
        i = 1
        
        for veiculo in portfolio:
            print(f'''
    VEICULO {i}:
    ----------------------------------------------------------------------------------------------------------------------
    PLACA: {veiculo.placa} | TIPO: {veiculo.tipo} | MARCA: {veiculo.marca} | MODELO: {veiculo.modelo}
    ANO: {veiculo.ano_fabricacao} | COR: {veiculo.cor} | PORTAS: {veiculo.portas} | COMBUSTIVEL: {veiculo.combustivel}
    ESTADO: {veiculo.conservacao} | QUILOMETRAGEM: {veiculo.quilometragem:.2f}Km | PRECO: R${veiculo.preco:.2f}
    STATUS: {veiculo.status}
    ______________________________________________________________________________________________________________________''')
            i += 1
        
        n = input('VOLTAR AO MENU [1]\n>>> ')
        if n != '1':
            print('ERRO: opcao invalida!')
            time.sleep(1)
        else:
            break
