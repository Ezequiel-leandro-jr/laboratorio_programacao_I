import customtkinter as ctk
from tkinter import RIGHT, LEFT, BOTH, Y
from classe_veiculo import Veiculo
from funcao_exibir import funcao_exibir
from crud_listar import listar
from cabecalhos import titulo_automarket, titulo_registrar

def cadastrar(portfolio):
    def register_vehicle():
        # Coletar dados do veículo
        tipo = var_tipo.get()
        combustivel = var_combustivel.get()
        conservacao = var_conservacao.get()
        status = var_status.get()
        placa = entry_placa.get().strip()
        marca = entry_marca.get().strip()
        modelo = entry_modelo.get().strip()
        cor = entry_cor.get().strip()
        ano_fabricacao = entry_ano.get().strip()
        portas = int(entry_portas.get().strip())
        quilometragem = float(entry_quilometragem.get().strip())
        preco = float(entry_preco.get().strip())
        
        # Criar novo veículo
        novo_veiculo = Veiculo(placa, tipo, marca, modelo, cor, ano_fabricacao, portas, combustivel, conservacao, quilometragem, preco, status)
        portfolio.append(novo_veiculo)
        
        # Mostrar mensagem de sucesso
        lbl_message.configure(text="Registro realizado com sucesso!", text_color="green")

    def new_register():
        # Limpar os campos para novo registro
        entry_placa.delete(0, ctk.END)
        entry_marca.delete(0, ctk.END)
        entry_modelo.delete(0, ctk.END)
        entry_cor.delete(0, ctk.END)
        entry_ano.delete(0, ctk.END)
        entry_portas.delete(0, ctk.END)
        entry_quilometragem.delete(0, ctk.END)
        entry_preco.delete(0, ctk.END)
        var_tipo.set('')
        var_combustivel.set('')
        var_conservacao.set('')
        var_status.set('')
        lbl_message.configure(text="")

    def list_vehicles():
        window.destroy()
        listar(portfolio)
    
    def close_window():
        window.destroy()

    # Criar a janela principal com um tamanho mais ajustado
    window = ctk.CTk()
    window.title("Cadastrar Veículo")
    window.geometry("500x650")

    # Criar canvas e frame para permitir scroll
    canvas = ctk.CTkCanvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = ctk.CTkScrollbar(window, orientation="vertical", command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame para conteúdo com o formulário
    frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    # Adicionar cabeçalhos
    lbl_title = ctk.CTkLabel(frame, text="Cadastrar Novo Veículo", font=("Helvetica", 16))
    lbl_title.grid(row=0, column=0, columnspan=2, pady=10)

    # Variáveis para campos de seleção
    var_tipo = ctk.StringVar()
    var_combustivel = ctk.StringVar()
    var_conservacao = ctk.StringVar()
    var_status = ctk.StringVar()

    # Campos de entrada
    lbl_placa = ctk.CTkLabel(frame, text="PLACA:")
    lbl_placa.grid(row=1, column=0, padx=10, pady=5, sticky='e')
    entry_placa = ctk.CTkEntry(frame)
    entry_placa.grid(row=1, column=1, padx=10, pady=5)

    lbl_tipo = ctk.CTkLabel(frame, text="TIPO:")
    lbl_tipo.grid(row=2, column=0, padx=10, pady=5, sticky='e')
    ctk.CTkOptionMenu(frame, values=["Camioneta", "Caminhonete", "Caminhão", "Carro", "Carreta", "Motocicleta", "Outro"], variable=var_tipo).grid(row=2, column=1, padx=10, pady=5)

    lbl_marca = ctk.CTkLabel(frame, text="MARCA:")
    lbl_marca.grid(row=3, column=0, padx=10, pady=5, sticky='e')
    entry_marca = ctk.CTkEntry(frame)
    entry_marca.grid(row=3, column=1, padx=10, pady=5)

    lbl_modelo = ctk.CTkLabel(frame, text="MODELO:")
    lbl_modelo.grid(row=4, column=0, padx=10, pady=5, sticky='e')
    entry_modelo = ctk.CTkEntry(frame)
    entry_modelo.grid(row=4, column=1, padx=10, pady=5)

    lbl_cor = ctk.CTkLabel(frame, text="COR:")
    lbl_cor.grid(row=5, column=0, padx=10, pady=5, sticky='e')
    entry_cor = ctk.CTkEntry(frame)
    entry_cor.grid(row=5, column=1, padx=10, pady=5)

    lbl_ano = ctk.CTkLabel(frame, text="ANO:")
    lbl_ano.grid(row=6, column=0, padx=10, pady=5, sticky='e')
    entry_ano = ctk.CTkEntry(frame)
    entry_ano.grid(row=6, column=1, padx=10, pady=5)

    lbl_portas = ctk.CTkLabel(frame, text="PORTAS:")
    lbl_portas.grid(row=7, column=0, padx=10, pady=5, sticky='e')
    entry_portas = ctk.CTkEntry(frame)
    entry_portas.grid(row=7, column=1, padx=10, pady=5)

    lbl_combustivel = ctk.CTkLabel(frame, text="COMBUSTÍVEL:")
    lbl_combustivel.grid(row=8, column=0, padx=10, pady=5, sticky='e')
    ctk.CTkOptionMenu(frame, values=["Gasolina", "GLP", "Etanol", "GNV", "Eletrico", "Hibrido", "Outro"], variable=var_combustivel).grid(row=8, column=1, padx=10, pady=5)

    lbl_conservacao = ctk.CTkLabel(frame, text="ESTADO DE CONSERVAÇÃO:")
    lbl_conservacao.grid(row=9, column=0, padx=10, pady=5, sticky='e')
    ctk.CTkOptionMenu(frame, values=["Novo", "Seminovo"], variable=var_conservacao).grid(row=9, column=1, padx=10, pady=5)

    lbl_quilometragem = ctk.CTkLabel(frame, text="QUILOMETRAGEM (KM):")
    lbl_quilometragem.grid(row=10, column=0, padx=10, pady=5, sticky='e')
    entry_quilometragem = ctk.CTkEntry(frame)
    entry_quilometragem.grid(row=10, column=1, padx=10, pady=5)

    lbl_preco = ctk.CTkLabel(frame, text="PREÇO (R$):")
    lbl_preco.grid(row=11, column=0, padx=10, pady=5, sticky='e')
    entry_preco = ctk.CTkEntry(frame)
    entry_preco.grid(row=11, column=1, padx=10, pady=5)

    lbl_status = ctk.CTkLabel(frame, text="STATUS:")
    lbl_status.grid(row=12, column=0, padx=10, pady=5, sticky='e')
    ctk.CTkOptionMenu(frame, values=["A venda", "Reservado", "Vendido", "Indisponível"], variable=var_status).grid(row=12, column=1, padx=10, pady=5)

    # Mensagem
    lbl_message = ctk.CTkLabel(frame, text="", font=("Helvetica", 12), text_color="red")
    lbl_message.grid(row=13, column=0, columnspan=2, pady=10)

    # Botões
    btn_register = ctk.CTkButton(frame, text="Registrar", command=register_vehicle)
    btn_register.grid(row=14, column=0, columnspan=2, pady=10)

    btn_new_register = ctk.CTkButton(frame, text="Novo Registro", command=new_register)
    btn_new_register.grid(row=15, column=0, columnspan=2, pady=5)

    btn_list_vehicles = ctk.CTkButton(frame, text="Listar Veículos", command=list_vehicles)
    btn_list_vehicles.grid(row=16, column=0, columnspan=2, pady=5)

    btn_close = ctk.CTkButton(frame, text="Voltar ao Menu", command=close_window)
    btn_close.grid(row=17, column=0, columnspan=2, pady=5)

    # Atualizar scrollregion após adicionar widgets
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    window.mainloop()

