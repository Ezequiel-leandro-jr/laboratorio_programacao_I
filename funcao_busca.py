def funcao_busca(portfolio):
    placa = input('PLACA: ')
    if placa:
        for veiculo in portfolio:
            if veiculo.placa == placa:
                return veiculo
    else:
        return

