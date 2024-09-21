import customtkinter as ctk
from funcao_placa import funcao_placa
from cabecalhos import titulo_listar
from tkinter import messagebox

# Inicializar lbl_total como None
lbl_total = None

def listar(portfolio):
    def update_list():
        # Limpar widgets existentes no frame_list
        for widget in frame_list.winfo_children():
            widget.destroy()

        # Atualizar a lista de veículos
        for i, veiculo in enumerate(portfolio, start=1):
            # Tenta converter quilometragem para float
            try:
                quilometragem = float(veiculo.quilometragem)
            except ValueError:
                quilometragem = 0.0  # Define valor padrão se a conversão falhar

            # Criar um frame para cada veículo, estilizado com bordas
            veiculo_frame = ctk.CTkFrame(frame_list, fg_color="#EDEDED", corner_radius=10)
            veiculo_frame.pack(pady=10, fill="x", padx=10)

            # Adicionar a descrição do veículo de forma estilizada
            ctk.CTkLabel(veiculo_frame, text=f"VEÍCULO {i}", font=("Helvetica", 14, "bold"), text_color="#1C1C1C").pack(pady=5)

            ctk.CTkLabel(veiculo_frame, text=f"PLACA: {veiculo.placa}  |  TIPO: {veiculo.tipo}  |  MARCA: {veiculo.marca}  |  MODELO: {veiculo.modelo}", 
                         font=("Helvetica", 12), text_color="#333333").pack(pady=2)

            ctk.CTkLabel(veiculo_frame, text=f"ANO: {veiculo.ano_fabricacao}  |  COR: {veiculo.cor}  |  PORTAS: {veiculo.portas}  |  COMBUSTÍVEL: {veiculo.combustivel}", 
                         font=("Helvetica", 12), text_color="#333333").pack(pady=2)

            ctk.CTkLabel(veiculo_frame, text=f"ESTADO: {veiculo.conservacao}  |  KM: {quilometragem:.2f} Km  |  PREÇO: R${veiculo.preco}", 
                         font=("Helvetica", 12), text_color="#333333").pack(pady=2)

            ctk.CTkLabel(veiculo_frame, text=f"STATUS: {veiculo.status}", 
                         font=("Helvetica", 12, "italic"), text_color="#1C1C1C").pack(pady=2)

        # Atualizar o lbl_total apenas se a janela ainda existir
        if window and window.winfo_exists():
            global lbl_total
            if lbl_total is None or not lbl_total.winfo_exists():
                lbl_total = ctk.CTkLabel(frame_list, text="")
                lbl_total.pack(pady=10)
            lbl_total.configure(text=f'TOTAL DE VEÍCULOS: {len(portfolio)}')

    def on_back():
        window.destroy()

    global window
    window = ctk.CTk()
    window.title("Listar Veículos")
    window.geometry("800x600")

    frame_list = ctk.CTkFrame(window)
    frame_list.pack(fill="both", expand=True, padx=20, pady=20)

    lbl_title = ctk.CTkLabel(frame_list, text="Lista de Veículos", font=("Helvetica", 16, "bold"))
    lbl_title.pack(pady=10)

    # Usar a palavra-chave global para lbl_total
    global lbl_total
    lbl_total = ctk.CTkLabel(frame_list, text="")
    lbl_total.pack(pady=10)

    update_list()

    btn_back = ctk.CTkButton(frame_list, text="VOLTAR AO MENU", command=on_back)
    btn_back.pack(pady=5)

    window.mainloop()
