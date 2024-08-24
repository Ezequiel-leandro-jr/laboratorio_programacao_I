# placa, tipo, marca, modelo, cor, ano_fabricacao, portas, combustivel, conservacao, quilometragem, preco, status
def funcao_exibir(veiculo):
    print(f'''
VEICULO:
----------------------------------------------------------------------------------------------------------------------
PLACA: {veiculo.placa} | TIPO: {veiculo.tipo} | MARCA: {veiculo.marca} | MODELO: {veiculo.modelo}
ANO: {veiculo.ano_fabricacao} | COR: {veiculo.cor} | PORTAS: {veiculo.portas} | COMBUSTIVEL: {veiculo.combustivel}
ESTADO: {veiculo.conservacao} | QUILOMETRAGEM: {veiculo.quilometragem:.2f}Km | PRECO: R${veiculo.preco:.2f}
STATUS: {veiculo.status}
______________________________________________________________________________________________________________________

''')