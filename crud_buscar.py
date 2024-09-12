import customtkinter as ctk
import tkinter
from funcao_busca import funcao_busca
from funcao_exibir import funcao_exibir
import crud_editar
import crud_deletar
from cabecalhos import titulo_automarket, titulo_buscar
from persistencia import salva_banco, cria_banco

portfolio = cria_banco()

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("light")  # Tema claro
ctk.set_default_color_theme("green")  # Tema verde

def buscar_interface(portfolio):
    # Criando a janela principal para a busca
    root = ctk.CTk()
    root.title("Buscar Veículo")
    root.geometry("600x500")
    
    # Frame principal
    frame = ctk.CTkFrame(root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Exibindo o título
    titulo_automarket(frame)
    titulo_buscar(frame)

    # Variável de entrada para a placa
    placa_var = ctk.StringVar()

    # Campo de entrada para a placa
    ctk.CTkLabel(frame, text="Digite a placa do veículo:", font=("Helvetica", 12)).pack(pady=10)
    placa_entry = ctk.CTkEntry(frame, textvariable=placa_var)
    placa_entry.pack(pady=5)

    # Função para buscar veículo
    def buscar_veiculo():
        placa = placa_var.get().strip().upper()  # Remove espaços e converte para maiúsculas
        veiculo = funcao_busca(portfolio, placa)
        
        if veiculo:
            resultado_frame.pack_forget()  # Limpa o frame anterior, se houver
            exibir_resultado(veiculo)
            salva_banco(portfolio)
        else:
            exibir_erro("Veículo não encontrado!")
            salva_banco(portfolio)

    # Botão de busca
    ctk.CTkButton(frame, text="Buscar", command=buscar_veiculo).pack(pady=10)

    # Frame para mostrar resultados ou mensagens de erro
    resultado_frame = ctk.CTkFrame(frame)
    resultado_frame.pack(pady=20)

    # Função para exibir resultado da busca
    def exibir_resultado(veiculo):
        # Limpando o frame de resultado
        for widget in resultado_frame.winfo_children():
            widget.destroy()

        # Exibindo o veículo encontrado
        funcao_exibir(veiculo, resultado_frame)

        # Opções após exibição
        ctk.CTkButton(resultado_frame, text="Editar", command=lambda: crud_editar).pack(pady=5)
        ctk.CTkButton(resultado_frame, text="Deletar", command=lambda: crud_deletar).pack(pady=5)
        ctk.CTkButton(resultado_frame, text="Nova Busca", command=nova_busca).pack(pady=5)
        ctk.CTkButton(resultado_frame, text="Voltar ao Menu", command=root.destroy).pack(pady=5)

    # Função para exibir erro
    def exibir_erro(mensagem):
        # Limpando o frame de resultado
        for widget in resultado_frame.winfo_children():
            widget.destroy()
        
        ctk.CTkLabel(resultado_frame, text=mensagem, font=("Helvetica", 12), fg_color="red").pack(pady=10)
        ctk.CTkButton(resultado_frame, text="Nova Busca", command=nova_busca).pack(pady=5)
        ctk.CTkButton(resultado_frame, text="Voltar ao Menu", command=root.destroy).pack(pady=5)

    # Função para realizar nova busca
    def nova_busca():
        resultado_frame.pack_forget()  # Limpa o frame de resultado
        placa_var.set("")  # Limpa o campo de entrada

    root.mainloop()
