import pandas as pd
import os
from classe_veiculo import Veiculo


def cria_banco():
    file = 'banco.xlsx'

    if os.path.exists(file):
        dfbanco = pd.read_excel(file)
        dfdict = dfbanco.to_dict(orient='records')
        lista_de_objetos = [Veiculo(**dados) for dados in dfdict]
        return lista_de_objetos
    else:
        portfolio = []
        return portfolio


def salva_banco(portfolio):
    file = 'banco.xlsx'
    
    lista_dicts = [Veiculo.__dict__ for Veiculo in portfolio]
    df = pd.DataFrame(lista_dicts)
    df.to_excel(file, index=False)
