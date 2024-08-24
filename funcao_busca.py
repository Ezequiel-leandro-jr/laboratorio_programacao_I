def funcao_busca(portfolio, placa):
    if placa:
        for veiculo in portfolio:
            if veiculo.placa == placa:
                return veiculo
    else:
        return

