import customtkinter as ctk
from funcao_busca import funcao_busca
from classe_veiculo import Veiculo
from funcao_exibir import funcao_exibir
from cabecalhos import titulo_automarket, titulo_editar
from persistencia import salva_banco, cria_banco
import tkinter

portfolio = cria_banco()

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("light")  # Tema claro
ctk.set_default_color_theme("green")  # Tema verde

def editar_interface(portfolio, placa):
    # Criando a janela principal para edição de veículos
    root = ctk.CTk()
    root.title("Editar Veículo")
    root.geometry("800x600")

    # Função para atualizar o veículo na lista e no índice
    def atualizar_veiculo(veiculo_atualizado):
        index = portfolio.index(veiculo)
        portfolio[index] = veiculo_atualizado
        salva_banco(portfolio)
        ctk.CTkLabel(root, text="EDIÇÃO REALIZADA COM SUCESSO!", font=("Helvetica", 14, "bold"), fg_color="green").pack(pady=10)
        root.after(2000, root.destroy)  # Fecha a janela após 2 segundos

    # Função para atualizar os campos com o veículo
    def atualizar_campos():
        veiculo_atualizado = veiculo.copy()
        # Atualiza os valores dos campos com os valores do veículo
        veiculo_atualizado.placa = placa_entry.get()
        veiculo_atualizado.tipo = tipo_var.get()
        veiculo_atualizado.marca = marca_entry.get()
        veiculo_atualizado.modelo = modelo_entry.get()
        veiculo_atualizado.cor = cor_entry.get()
        veiculo_atualizado.ano_fabricacao = ano_entry.get()
        veiculo_atualizado.portas = portas_entry.get()
        veiculo_atualizado.combustivel = combustivel_var.get()
        veiculo_atualizado.conservacao = conservacao_var.get()
        veiculo_atualizado.quilometragem = quilometragem_entry.get()
        veiculo_atualizado.preco = preco_entry.get()
        veiculo_atualizado.status = status_var.get()
        atualizar_veiculo(veiculo_atualizado)

    # Função para carregar o veículo
    veiculo = funcao_busca(portfolio, placa)
    if not veiculo:
        ctk.CTkLabel(root, text="Veículo não encontrado!", font=("Helvetica", 14, "bold"), fg_color="red").pack(pady=10)
        root.after(2000, root.destroy)  # Fecha a janela após 2 segundos
        return

    # Frame principal
    frame = ctk.CTkFrame(root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Exibindo o título
    titulo_automarket(frame)
    titulo_editar(frame)

    # Dados do veículo
    placa_entry = ctk.CTkEntry(frame, width=200)
    placa_entry.insert(0, veiculo.placa)

    tipo_var = ctk.StringVar(value=veiculo.tipo)
    tipo_menu = ctk.CTkOptionMenu(frame, variable=tipo_var, values=[
        'Camioneta', 'Caminhonete', 'Caminhão', 'Carro', 'Carreta', 'Motocicleta', 'Outro'])

    marca_entry = ctk.CTkEntry(frame, width=200)
    marca_entry.insert(0, veiculo.marca)

    modelo_entry = ctk.CTkEntry(frame, width=200)
    modelo_entry.insert(0, veiculo.modelo)

    cor_entry = ctk.CTkEntry(frame, width=200)
    cor_entry.insert(0, veiculo.cor)

    ano_entry = ctk.CTkEntry(frame, width=200)
    ano_entry.insert(0, veiculo.ano_fabricacao)

    portas_entry = ctk.CTkEntry(frame, width=200)
    portas_entry.insert(0, veiculo.portas)

    combustivel_var = ctk.StringVar(value=veiculo.combustivel)
    combustivel_menu = ctk.CTkOptionMenu(frame, variable=combustivel_var, values=[
        'Gasolina', 'GLP', 'Etanol', 'GNV', 'Elétrico', 'Híbrido', 'Outro'])

    conservacao_var = ctk.StringVar(value=veiculo.conservacao)
    conservacao_menu = ctk.CTkOptionMenu(frame, variable=conservacao_var, values=[
        'Novo', 'Seminovo'])

    quilometragem_entry = ctk.CTkEntry(frame, width=200)
    quilometragem_entry.insert(0, veiculo.quilometragem)

    preco_entry = ctk.CTkEntry(frame, width=200)
    preco_entry.insert(0, veiculo.preco)

    status_var = ctk.StringVar(value=veiculo.status)
    status_menu = ctk.CTkOptionMenu(frame, variable=status_var, values=[
        'À venda', 'Reservado', 'Vendido', 'Indisponível'])

    # Adicionando os widgets ao frame
    ctk.CTkLabel(frame, text="Placa:").pack(pady=5)
    placa_entry.pack(pady=5)
    
    ctk.CTkLabel(frame, text="Tipo:").pack(pady=5)
    tipo_menu.pack(pady=5)

    ctk.CTkLabel(frame, text="Marca:").pack(pady=5)
    marca_entry.pack(pady=5)

    ctk.CTkLabel(frame, text="Modelo:").pack(pady=5)
    modelo_entry.pack(pady=5)

    ctk.CTkLabel(frame, text="Cor:").pack(pady=5)
    cor_entry.pack(pady=5)

    ctk.CTkLabel(frame, text="Ano de Fabricação:").pack(pady=5)
    ano_entry.pack(pady=5)

    ctk.CTkLabel(frame, text="Portas:").pack(pady=5)
    portas_entry.pack(pady=5)

    ctk.CTkLabel(frame, text="Combustível:").pack(pady=5)
    combustivel_menu.pack(pady=5)

    ctk.CTkLabel(frame, text="Conservação:").pack(pady=5)
    conservacao_menu.pack(pady=5)

    ctk.CTkLabel(frame, text="Quilometragem (KM):").pack(pady=5)
    quilometragem_entry.pack(pady=5)

    ctk.CTkLabel(frame, text="Preço (R$):").pack(pady=5)
    preco_entry.pack(pady=5)

    ctk.CTkLabel(frame, text="Status:").pack(pady=5)
    status_menu.pack(pady=5)

    # Botão para salvar as edições
    save_button = ctk.CTkButton(frame, text="Salvar Edição", command=atualizar_campos)
    save_button.pack(pady=10)

    # Botão para voltar ao menu principal
    back_button = ctk.CTkButton(frame, text="Voltar ao Menu", command=root.destroy)
    back_button.pack(pady=10)

    root.mainloop()
