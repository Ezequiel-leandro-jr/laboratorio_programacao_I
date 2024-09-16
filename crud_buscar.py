import customtkinter as ctk
from funcao_busca import funcao_busca
from funcao_exibir import funcao_exibir
from funcao_placa import funcao_placa
from crud_editar import editar
from crud_deletar import deletar
from cabecalhos import titulo_automarket, titulo_buscar

def buscar(portfolio, placa):
    def on_edit():
        nonlocal placa
        new_placa = funcao_placa(portfolio, placa)
        if new_placa:
            editar(portfolio, new_placa)
            window.destroy()

    def on_delete():
        nonlocal placa
        deletar(portfolio, placa)
        window.destroy()

    def on_new_search():
        nonlocal placa
        placa = funcao_placa(portfolio, placa)
        update_vehicle_info()
    
    def on_close():
        window.destroy()
    
    def update_vehicle_info():
        nonlocal placa
        veiculo = funcao_busca(portfolio, placa)
        if veiculo:
            lbl_vehicle_info.configure(text=f'''
            PLACA: {veiculo.placa}
            TIPO: {veiculo.tipo}
            MARCA: {veiculo.marca}
            MODELO: {veiculo.modelo}
            ANO: {veiculo.ano_fabricacao}
            COR: {veiculo.cor}
            PORTAS: {veiculo.portas}
            COMBUSTÍVEL: {veiculo.combustivel}
            ESTADO: {veiculo.conservacao}
            QUILOMETRAGEM: {veiculo.quilometragem:.2f}Km
            PREÇO: R${veiculo.preco:.2f}
            STATUS: {veiculo.status}
            ''')
            lbl_vehicle_info.pack(pady=10)
            btn_edit.pack(pady=5)
            btn_delete.pack(pady=5)
        else:
            lbl_vehicle_info.configure(text="ERRO: Veículo não encontrado!")
            lbl_vehicle_info.pack(pady=10)
            btn_new_search.pack(pady=5)
            btn_close.pack(pady=5)
    
    # Criar janela principal
    window = ctk.CTk()
    window.title("Buscar Veículo")
    window.geometry("600x400")

    # Adicionar cabeçalhos
    frame = ctk.CTkFrame(window)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    lbl_title = ctk.CTkLabel(frame, text="Buscar Veículo", font=("Helvetica", 16))
    lbl_title.pack(pady=10)
    
    lbl_vehicle_info = ctk.CTkLabel(frame, text="", anchor="w", justify="left", font=("Helvetica", 12))

    # Botões
    btn_edit = ctk.CTkButton(frame, text="EDITAR", command=on_edit)
    btn_delete = ctk.CTkButton(frame, text="DELETAR", command=on_delete)
    btn_new_search = ctk.CTkButton(frame, text="NOVA BUSCA", command=on_new_search)
    btn_close = ctk.CTkButton(frame, text="FECHAR", command=on_close)

    # Atualizar informações do veículo
    update_vehicle_info()

    window.mainloop()
