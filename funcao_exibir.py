import customtkinter as ctk
import tkinter

def funcao_exibir(veiculo, parent_frame):
    """
    Exibe os detalhes de um veículo em uma interface gráfica.
    
    Args:
        veiculo (object): Objeto que representa o veículo.
        parent_frame (ctk.CTkFrame): Frame pai onde os detalhes do veículo serão exibidos.
    """
    # Frame para exibir detalhes do veículo
    veiculo_frame = ctk.CTkFrame(parent_frame, border_width=1, border_color="gray")
    veiculo_frame.pack(pady=5, padx=5, fill="x")

    detalhes = (
        f"PLACA: {veiculo.placa} | TIPO: {veiculo.tipo} | MARCA: {veiculo.marca} | MODELO: {veiculo.modelo}\n"
        f"ANO: {veiculo.ano_fabricacao} | COR: {veiculo.cor} | PORTAS: {veiculo.portas} | COMBUSTÍVEL: {veiculo.combustivel}\n"
        f"ESTADO: {veiculo.conservacao} | QUILOMETRAGEM: {veiculo.quilometragem:.2f}Km | PREÇO: R${veiculo.preco:.2f}\n"
        f"STATUS: {veiculo.status}"
    )

    # Label para exibir os detalhes do veículo
    ctk.CTkLabel(veiculo_frame, text=detalhes, font=("Helvetica", 12), justify="left", wraplength=700).pack(padx=10, pady=5)
