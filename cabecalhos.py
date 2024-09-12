import customtkinter as ctk
import tkinter

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("light")  # Tema claro
ctk.set_default_color_theme("green")  # Tema verde

def titulo_automarket(frame):
    """ Exibe o título principal do sistema AutoMarket """
    label = ctk.CTkLabel(frame, text="===|| AUTOMARKET ||===", 
                         font=("Helvetica", 20, "bold"), text_color="#228B22", fg_color="white", bg_color="white")
    label.pack(pady=20)

def titulo_buscar(frame):
    """ Exibe o cabeçalho para o módulo de busca de veículos """
    label = ctk.CTkLabel(frame, text="BUSCAR VEÍCULO", 
                         font=("Helvetica", 16, "bold"), text_color="#228B22", fg_color="white", bg_color="white")
    label.pack(pady=10)

def titulo_deletar(frame):
    """ Exibe o cabeçalho para o módulo de deleção de veículos """
    label = ctk.CTkLabel(frame, text="DELETAR VEÍCULO", 
                         font=("Helvetica", 16, "bold"), text_color="#228B22", fg_color="white", bg_color="white")
    label.pack(pady=10)

def titulo_editar(frame):
    """ Exibe o cabeçalho para o módulo de edição de veículos """
    label = ctk.CTkLabel(frame, text="EDITAR VEÍCULO", 
                         font=("Helvetica", 16, "bold"), text_color="#228B22", fg_color="white", bg_color="white")
    label.pack(pady=10)

def titulo_listar(frame):
    """ Exibe o cabeçalho para o módulo de listagem de veículos """
    label = ctk.CTkLabel(frame, text="LISTAGEM GERAL", 
                         font=("Helvetica", 16, "bold"), text_color="#228B22", fg_color="white", bg_color="white")
    label.pack(pady=10)

def titulo_registrar(frame):
    """ Exibe o cabeçalho para o módulo de registro de veículos """
    label = ctk.CTkLabel(frame, text="REGISTRAR VEÍCULO", 
                         font=("Helvetica", 16, "bold"), text_color="#228B22", fg_color="white", bg_color="white")
    label.pack(pady=10)