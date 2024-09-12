from classe_veiculo import Veiculo
from persistencia import cria_banco, salva_banco
import crud_registrar 
import crud_editar 
import crud_buscar 
import crud_listar
import crud_deletar
from cabecalhos import titulo_automarket, titulo_buscar, titulo_deletar, titulo_editar, titulo_registrar, titulo_listar
import time
import os
import pandas
import customtkinter as ctk
import tkinter

portfolio = cria_banco()

# Definindo a aparência padrão
ctk.set_appearance_mode("light")  # Usa tema claro para combinação com o branco
ctk.set_default_color_theme("green")  # Define o tema de cores como verde

# Criando a janela principal
app = ctk.CTk()
app.title("AutoMarket")
app.geometry("400x500")
app.configure(bg="white")  # Fundo branco para harmonizar

# Adicionando os botões ao menu principal
titulo_automarket()

botao_registrar = ctk.CTkButton(app, text="Registrar Veículo", command=crud_registrar, fg_color="#228B22")  # Verde
botao_registrar.pack(pady=10)

botao_buscar = ctk.CTkButton(app, text="Buscar Veículo", command=crud_buscar, fg_color="#228B22")  # Verde
botao_buscar.pack(pady=10)

botao_editar = ctk.CTkButton(app, text="Editar Veículo", command=crud_editar, fg_color="#228B22")  # Verde
botao_editar.pack(pady=10)

botao_listar = ctk.CTkButton(app, text="Listar Veículos", command=crud_listar, fg_color="#228B22")  # Verde
botao_listar.pack(pady=10)

botao_deletar = ctk.CTkButton(app, text="Deletar Veículo", command=crud_deletar, fg_color="#228B22")  # Verde
botao_deletar.pack(pady=10)

botao_sair = ctk.CTkButton(app, text="Sair do Sistema", command=app.quit, fg_color="#228B22")  # Verde
botao_sair.pack(pady=20)

salva_banco(portfolio)

# Executando a interface gráfica
app.mainloop()
