import customtkinter as ctk

def funcao_exibir(veiculo):
    def on_close():
        window.destroy()

    window = ctk.CTk()
    window.title("Exibir Veículo")
    window.geometry("600x400")

    frame = ctk.CTkFrame(window)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    lbl_title = ctk.CTkLabel(frame, text="Detalhes do Veículo", font=("Helvetica", 16))
    lbl_title.pack(pady=10)

    details = f'''
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
    '''

    lbl_details = ctk.CTkLabel(frame, text=details, anchor="w", justify="left", font=("Helvetica", 12))
    lbl_details.pack(pady=10)

    btn_close = ctk.CTkButton(frame, text="FECHAR", command=on_close)
    btn_close.pack(pady=5)

    window.mainloop()
