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
