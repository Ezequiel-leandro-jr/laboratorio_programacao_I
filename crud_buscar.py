import customtkinter as ctk
from funcao_busca import funcao_busca
from funcao_placa import funcao_placa

def buscar(portfolio, placa):
    def on_edit():
        nonlocal placa
        new_placa = funcao_placa(portfolio, placa)
        if new_placa:
            placa = new_placa
            update_vehicle_info()
    
    def on_delete():
        nonlocal placa
        # Função para deletar veículo
        # Adicione a lógica para deletar o veículo aqui
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
        
        # Limpar o frame antes de adicionar novos widgets
        for widget in detalhes_frame.winfo_children():
            widget.destroy()

        if veiculo:
            # Adicionar a descrição do veículo de forma estilizada
            ctk.CTkLabel(detalhes_frame, text="DETALHES DO VEÍCULO", font=("Helvetica", 16, "bold"), text_color="#1C1C1C").pack(pady=5)

            ctk.CTkLabel(detalhes_frame, text=f"PLACA: {veiculo.placa}  |  TIPO: {veiculo.tipo}  |  MARCA: {veiculo.marca}  |  MODELO: {veiculo.modelo}", 
                         font=("Helvetica", 12), text_color="#333333").pack(pady=2)

            ctk.CTkLabel(detalhes_frame, text=f"ANO: {veiculo.ano_fabricacao}  |  COR: {veiculo.cor}  |  PORTAS: {veiculo.portas}  |  COMBUSTÍVEL: {veiculo.combustivel}", 
                         font=("Helvetica", 12), text_color="#333333").pack(pady=2)

            ctk.CTkLabel(detalhes_frame, text=f"ESTADO: {veiculo.conservacao}  |  KM: {veiculo.quilometragem:.2f} Km  |  PREÇO: R${veiculo.preco:.2f}", 
                         font=("Helvetica", 12), text_color="#333333").pack(pady=2)

            ctk.CTkLabel(detalhes_frame, text=f"STATUS: {veiculo.status}", 
                         font=("Helvetica", 12, "italic"), text_color="#1C1C1C").pack(pady=2)

            # Mostrar os botões
            btn_edit.pack(pady=5, fill="x")
            btn_delete.pack(pady=5, fill="x")
        else:
            lbl_vehicle_info.configure(text="ERRO: Veículo não encontrado!")
            lbl_vehicle_info.pack(pady=10, fill="both", expand=True)
            btn_new_search.pack(pady=5, fill="x")
            btn_close.pack(pady=5, fill="x")
    
    # Criar janela principal
    window = ctk.CTk()
    window.title("Buscar Veículo")
    window.geometry("600x400")

    # Adicionar cabeçalhos
    frame = ctk.CTkFrame(window, border_width=2, corner_radius=10)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    lbl_title = ctk.CTkLabel(frame, text="Buscar Veículo", font=("Helvetica", 18, "bold"), text_color="#333333")
    lbl_title.pack(pady=10)

    lbl_vehicle_info = ctk.CTkLabel(frame, text="", anchor="w", justify="left", font=("Helvetica", 12), text_color="#333333")
    
    # Frame para detalhes do veículo
    detalhes_frame = ctk.CTkFrame(frame)
    detalhes_frame.pack(padx=20, pady=10, fill='both', expand=True)

    # Botões
    btn_edit = ctk.CTkButton(frame, text="EDITAR", command=on_edit, fg_color="green", hover_color="darkgreen")
    btn_delete = ctk.CTkButton(frame, text="DELETAR", command=on_delete, fg_color="red", hover_color="darkred")
    btn_new_search = ctk.CTkButton(frame, text="NOVA BUSCA", command=on_new_search, fg_color="orange", hover_color="darkorange")
    btn_close = ctk.CTkButton(frame, text="FECHAR", command=on_close, fg_color="gray", hover_color="darkgray")

    # Atualizar informações do veículo
    update_vehicle_info()

    window.mainloop()
