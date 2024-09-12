import customtkinter as ctk
from funcao_busca import funcao_busca
from funcao_exibir import funcao_exibir
from cabecalhos import titulo_automarket, titulo_deletar
from persistencia import salva_banco, cria_banco
import tkinter

portfolio = cria_banco()


def deletar_interface(portfolio):
    # Função para deletar um veículo
    def deletar_veiculo():
        placa = placa_entry.get().strip()
        if placa:  # Verifica se a placa não está vazia
            veiculo = funcao_busca(portfolio, placa)
            if veiculo:
                portfolio.remove(veiculo)
                salva_banco(portfolio)
                resultado_label.config(text="Veículo deletado com sucesso!")
                placa_entry.delete(0, 'end')
                deletar_outro()
            else:
                resultado_label.config(text="Erro: Veículo não encontrado!")
                salva_banco(portfolio)
                
        else:
            resultado_label.config(text="Erro: Placa não pode estar vazia!")
            salva_banco(portfolio)

    # Função para exibir a opção de deletar outro veículo
    def deletar_outro():
        # Atualiza o texto do botão para deletar outro veículo
        deletar_button.config(text="Deletar Outro Veículo", command=lambda: placa_entry.focus_set())
        resultado_label.after(2000, lambda: placa_entry.delete(0, 'end'))  # Limpa a entrada após 2 segundos

    # Função para retornar ao menu principal
    def voltar_ao_menu():
        root.destroy()  # Fecha a janela de deleção

    # Configuração inicial do CustomTkinter
    ctk.set_appearance_mode("light")  # Tema claro
    ctk.set_default_color_theme("green")  # Tema verde

    # Criando a janela principal para deletar veículos
    root = ctk.CTk()
    root.title("Deletar Veículo")
    root.geometry("800x600")

    # Frame principal
    frame = ctk.CTkFrame(root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Exibindo o título
    titulo_automarket(frame)
    titulo_deletar(frame)

    # Frame de deletar
    deletar_frame = ctk.CTkFrame(frame)
    deletar_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Entrada para a placa do veículo
    placa_label = ctk.CTkLabel(deletar_frame, text="Digite a placa do veículo:", font=("Helvetica", 14))
    placa_label.pack(pady=10)
    placa_entry = ctk.CTkEntry(deletar_frame, placeholder_text="PLACA")
    placa_entry.pack(pady=5)

    # Botão para deletar o veículo
    deletar_button = ctk.CTkButton(deletar_frame, text="Deletar Veículo", command=deletar_veiculo)
    deletar_button.pack(pady=10)

    # Label para mostrar o resultado
    resultado_label = ctk.CTkLabel(deletar_frame, text="", font=("Helvetica", 14))
    resultado_label.pack(pady=10)

    # Botão para voltar ao menu principal
    voltar_button = ctk.CTkButton(frame, text="Voltar ao Menu", command=voltar_ao_menu)
    voltar_button.pack(pady=10)

    root.mainloop()
