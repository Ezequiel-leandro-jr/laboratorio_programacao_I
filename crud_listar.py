import customtkinter as ctk
import crud_editar
import crud_deletar
from cabecalhos import titulo_automarket, titulo_listar
from persistencia import salva_banco, cria_banco
import tkinter

portfolio = cria_banco()

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("light")  # Tema claro
ctk.set_default_color_theme("green")  # Tema verde

def listar_interface(portfolio):
    # Criando a janela principal para listar veículos
    root = ctk.CTk()
    root.title("Listar Veículos")
    root.geometry("800x600")

    # Frame principal
    frame = ctk.CTkFrame(root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Exibindo o título
    titulo_automarket(frame)
    titulo_listar(frame)

    # Frame de listagem
    listagem_frame = ctk.CTkFrame(frame)
    listagem_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Função para exibir a lista de veículos
    def exibir_veiculos():
        # Limpa o frame de listagem para evitar sobreposição
        for widget in listagem_frame.winfo_children():
            widget.destroy()

        if not portfolio:
            ctk.CTkLabel(listagem_frame, text="Nenhum veículo encontrado!", font=("Helvetica", 14)).pack(pady=10)
            return

        # Exibe cada veículo na lista
        i = 1
        for veiculo in portfolio:
            veiculo_frame = ctk.CTkFrame(listagem_frame, border_width=1)
            veiculo_frame.pack(pady=5, padx=5, fill="x")

            detalhes = (
                f"VEÍCULO {i}:\n"
                f"PLACA: {veiculo.placa} | TIPO: {veiculo.tipo} | MARCA: {veiculo.marca} | MODELO: {veiculo.modelo}\n"
                f"ANO: {veiculo.ano_fabricacao} | COR: {veiculo.cor} | PORTAS: {veiculo.portas} | COMBUSTÍVEL: {veiculo.combustivel}\n"
                f"ESTADO: {veiculo.conservacao} | QUILOMETRAGEM: {veiculo.quilometragem:.2f}Km | PREÇO: R${veiculo.preco:.2f}\n"
                f"STATUS: {veiculo.status}"
            )

            ctk.CTkLabel(veiculo_frame, text=detalhes, font=("Helvetica", 12), justify="left").pack(padx=10, pady=5)
            # Botões de Editar e Deletar para cada veículo
            ctk.CTkButton(veiculo_frame, text="Editar", command=lambda: crud_editar).pack(side="left", padx=5, pady=5)
            ctk.CTkButton(veiculo_frame, text="Deletar", command=lambda: crud_deletar).pack(side="left", padx=5, pady=5)

            i += 1
        
        # Exibe o total de veículos
        total_label = ctk.CTkLabel(listagem_frame, text=f"\nTOTAL DE VEÍCULOS: {i - 1}", font=("Helvetica", 14, "bold"))
        total_label.pack(pady=10)
        salva_banco(portfolio)

    # Função para editar o veículo
    def editar_veiculo(veiculo):
        root.destroy()  # Fecha a janela de listagem
        editar(portfolio, veiculo.placa)  # Chama a função de editar

    # Função para deletar o veículo
    def deletar_veiculo(veiculo):
        root.destroy()  # Fecha a janela de listagem
        deletar(portfolio, veiculo.placa)  # Chama a função de deletar

    # Função para retornar ao menu principal
    def voltar_ao_menu():
        root.destroy()  # Fecha a janela de listagem

    # Botões de controle
    botoes_frame = ctk.CTkFrame(frame)
    botoes_frame.pack(pady=10)

    # Botão para voltar ao menu principal
    ctk.CTkButton(botoes_frame, text="Voltar ao Menu", command=voltar_ao_menu).pack(padx=5, pady=5)

    # Exibir a lista de veículos inicialmente
    exibir_veiculos()

    root.mainloop()
