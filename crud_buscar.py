import customtkinter as ctk
from funcao_busca import funcao_busca
from funcao_placa import funcao_placa

def buscar(portfolio, placa):
    def on_edit():
        nonlocal placa
        new_placa = funcao_placa(portfolio, placa)
        if new_placa:
            window.destroy()

    def on_delete():
        nonlocal placa
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
            vehicle_info_text = (
                f"PLACA: {veiculo.placa}\n"
                f"TIPO: {veiculo.tipo}\n"
                f"MARCA: {veiculo.marca}\n"
                f"MODELO: {veiculo.modelo}\n"
                f"ANO: {veiculo.ano_fabricacao}\n"
                f"COR: {veiculo.cor}\n"
                f"PORTAS: {veiculo.portas}\n"
                f"COMBUSTÍVEL: {veiculo.combustivel}\n"
                f"ESTADO: {veiculo.conservacao}\n"
                f"QUILOMETRAGEM: {veiculo.quilometragem:.2f} Km\n"
                f"PREÇO: R${veiculo.preco:.2f}\n"
                f"STATUS: {veiculo.status}\n"
            )
            lbl_vehicle_info.configure(text=vehicle_info_text)
            lbl_vehicle_info.pack(pady=10, fill="both", expand=True)
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
    window.configure(bg_color="#f0f0f0")

    # Adicionar cabeçalhos
    frame = ctk.CTkFrame(window, bg_color="#ffffff", border_width=2, corner_radius=10)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    lbl_title = ctk.CTkLabel(frame, text="Buscar Veículo", font=("Helvetica", 18, "bold"), bg_color="#ffffff", text_color="#333333")
    lbl_title.pack(pady=10)

    lbl_vehicle_info = ctk.CTkLabel(frame, text="", anchor="w", justify="left", font=("Helvetica", 12), bg_color="#ffffff", text_color="#333333")
    
    # Botões
    btn_edit = ctk.CTkButton(frame, text="EDITAR", command=on_edit, fg_color="green", hover_color="darkgreen")
    btn_delete = ctk.CTkButton(frame, text="DELETAR", command=on_delete, fg_color="red", hover_color="darkred")
    btn_new_search = ctk.CTkButton(frame, text="NOVA BUSCA", command=on_new_search, fg_color="orange", hover_color="darkorange")
    btn_close = ctk.CTkButton(frame, text="FECHAR", command=on_close, fg_color="gray", hover_color="darkgray")

    # Atualizar informações do veículo
    update_vehicle_info()

    window.mainloop()
