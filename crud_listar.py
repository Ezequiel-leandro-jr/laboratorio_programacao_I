import customtkinter as ctk
from crud_editar import editar
from funcao_placa import funcao_placa
from crud_deletar import deletar
from cabecalhos import titulo_listar
from tkinter import messagebox

def listar(portfolio):
    def update_list():
        for widget in frame_list.winfo_children():
            widget.destroy()

        for i, veiculo in enumerate(portfolio, start=1):
            ctk.CTkLabel(frame_list, text=f'''
    VEÍCULO {i}:
    ----------------------------------------------------------------------------------------------------------------------
    PLACA: {veiculo.placa} | TIPO: {veiculo.tipo} | MARCA: {veiculo.marca} | MODELO: {veiculo.modelo}
    ANO: {veiculo.ano_fabricacao} | COR: {veiculo.cor} | PORTAS: {veiculo.portas} | COMBUSTÍVEL: {veiculo.combustivel}
    ESTADO: {veiculo.conservacao} | QUILOMETRAGEM: {veiculo.quilometragem:.2f}Km | PREÇO: R${veiculo.preco:.2f}
    STATUS: {veiculo.status}
    ----------------------------------------------------------------------------------------------------------------------
    ''', text_color="black", font=("Helvetica", 12)).pack(pady=10)

        lbl_total.config(text=f'TOTAL DE VEÍCULOS: {len(portfolio)}')

    def on_edit():
        placa = funcao_placa(portfolio)
        if placa:
            editar(portfolio, placa)
            update_list()

    def on_delete():
        placa = funcao_placa(portfolio)
        if placa:
            deletar(portfolio, placa)
            update_list()

    def on_back():
        window.destroy()

    window = ctk.CTk()
    window.title("Listar Veículos")
    window.geometry("800x600")

    frame_list = ctk.CTkFrame(window)
    frame_list.pack(fill="both", expand=True, padx=20, pady=20)

    lbl_title = ctk.CTkLabel(frame_list, text="Lista de Veículos", font=("Helvetica", 16))
    lbl_title.pack(pady=10)

    lbl_total = ctk.CTkLabel(frame_list, text="")
    lbl_total.pack(pady=10)

    update_list()

    btn_edit = ctk.CTkButton(frame_list, text="EDITAR VEÍCULO", command=on_edit)
    btn_edit.pack(pady=5)

    btn_delete = ctk.CTkButton(frame_list, text="DELETAR VEÍCULO", command=on_delete)
    btn_delete.pack(pady=5)

    btn_back = ctk.CTkButton(frame_list, text="VOLTAR AO MENU", command=on_back)
    btn_back.pack(pady=5)

    window.mainloop()
