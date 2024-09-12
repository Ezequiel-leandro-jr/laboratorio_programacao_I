import customtkinter as ctk
from classe_veiculo import Veiculo
from funcao_exibir import funcao_exibir
from crud_listar import listar
from cabecalhos import titulo_registrar
from persistencia import salva_banco, cria_banco
import tkinter

portfolio = cria_banco()

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("light")  # Tema claro
ctk.set_default_color_theme("green")  # Tema verde

def cadastrar(portfolio):
    # Criando a janela principal para o cadastro
    root = ctk.CTk()
    root.title("Registrar Veículo")
    root.geometry("600x600")
    
    # Frame para o cabeçalho e conteúdo
    frame = ctk.CTkFrame(root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Exibindo o título
    titulo_registrar(frame)
    
    # Variáveis de entrada
    placa_var = ctk.StringVar()
    tipo_var = ctk.StringVar(value="Selecionar Tipo")
    marca_var = ctk.StringVar()
    modelo_var = ctk.StringVar()
    cor_var = ctk.StringVar()
    ano_var = ctk.StringVar()
    portas_var = ctk.StringVar()
    combustivel_var = ctk.StringVar(value="Selecionar Combustível")
    conservacao_var = ctk.StringVar(value="Selecionar Conservação")
    quilometragem_var = ctk.StringVar()
    preco_var = ctk.StringVar()
    status_var = ctk.StringVar(value="Selecionar Status")
    
    # Campos de entrada de dados
    entries = [
        ("Placa:", placa_var),
        ("Marca:", marca_var),
        ("Modelo:", modelo_var),
        ("Cor:", cor_var),
        ("Ano de Fabricação:", ano_var),
        ("Portas:", portas_var),
        ("Quilometragem (km):", quilometragem_var),
        ("Preço (R$):", preco_var)
    ]
    
    # Criando rótulos e entradas
    for idx, (label_text, var) in enumerate(entries):
        ctk.CTkLabel(frame, text=label_text, font=("Helvetica", 12)).grid(row=idx, column=0, pady=5, padx=10, sticky="e")
        ctk.CTkEntry(frame, textvariable=var).grid(row=idx, column=1, pady=5, padx=10, sticky="w")
    
    # Menus de opções
    tipos = ["Camioneta", "Caminhonete", "Caminhão", "Carro", "Carreta", "Motocicleta", "Outro"]
    combustiveis = ["Gasolina", "GLP", "Etanol", "GNV", "Elétrico", "Híbrido", "Outro"]
    conservacoes = ["Novo", "Seminovo"]
    status_opcoes = ["À venda", "Reservado", "Vendido", "Indisponível"]

    ctk.CTkLabel(frame, text="Tipo:", font=("Helvetica", 12)).grid(row=len(entries), column=0, pady=5, padx=10, sticky="e")
    ctk.CTkOptionMenu(frame, values=tipos, variable=tipo_var).grid(row=len(entries), column=1, pady=5, padx=10, sticky="w")

    ctk.CTkLabel(frame, text="Combustível:", font=("Helvetica", 12)).grid(row=len(entries) + 1, column=0, pady=5, padx=10, sticky="e")
    ctk.CTkOptionMenu(frame, values=combustiveis, variable=combustivel_var).grid(row=len(entries) + 1, column=1, pady=5, padx=10, sticky="w")

    ctk.CTkLabel(frame, text="Conservação:", font=("Helvetica", 12)).grid(row=len(entries) + 2, column=0, pady=5, padx=10, sticky="e")
    ctk.CTkOptionMenu(frame, values=conservacoes, variable=conservacao_var).grid(row=len(entries) + 2, column=1, pady=5, padx=10, sticky="w")

    ctk.CTkLabel(frame, text="Status:", font=("Helvetica", 12)).grid(row=len(entries) + 3, column=0, pady=5, padx=10, sticky="e")
    ctk.CTkOptionMenu(frame, values=status_opcoes, variable=status_var).grid(row=len(entries) + 3, column=1, pady=5, padx=10, sticky="w")
    
    # Função de salvar o veículo
    def salvar_veiculo():
        novo_veiculo = Veiculo(
            placa_var.get(),
            tipo_var.get(),
            marca_var.get(),
            modelo_var.get(),
            cor_var.get(),
            ano_var.get(),
            int(portas_var.get()),
            combustivel_var.get(),
            conservacao_var.get(),
            float(quilometragem_var.get()),
            float(preco_var.get()),
            status_var.get()
        )
        portfolio.append(novo_veiculo)
        funcao_exibir(novo_veiculo)
        salva_banco(portfolio)
        mostrar_opcoes_apos_registro(novo_veiculo)

    # Botão para salvar
    ctk.CTkButton(frame, text="Registrar Veículo", command=salvar_veiculo).grid(row=len(entries) + 4, column=0, columnspan=2, pady=20)
    
    # Função para exibir opções após o registro
    def mostrar_opcoes_apos_registro(novo_veiculo):
        # Criando uma nova janela para as opções
        opcoes_window = ctk.CTkToplevel(root)
        opcoes_window.title("Registro Realizado")
        opcoes_window.geometry("400x300")
        
        # Exibição de mensagem de sucesso
        ctk.CTkLabel(opcoes_window, text="REGISTRO REALIZADO COM SUCESSO!", font=("Helvetica", 14, "bold")).pack(pady=20)
        
        # Botões de opção
        def novo_registro():
            opcoes_window.destroy()
            cadastrar(portfolio)

        def listar_veiculos():
            opcoes_window.destroy()
            listar(portfolio)
        
        def voltar_menu():
            opcoes_window.destroy()
            root.destroy()
        
        ctk.CTkButton(opcoes_window, text="Novo Registro", command=novo_registro).pack(pady=5)
        ctk.CTkButton(opcoes_window, text="Listar Veículos", command=listar_veiculos).pack(pady=5)
        ctk.CTkButton(opcoes_window, text="Voltar ao Menu", command=voltar_menu).pack(pady=5)
    
    root.mainloop()
