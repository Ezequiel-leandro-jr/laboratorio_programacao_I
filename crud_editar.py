import customtkinter as ctk
from funcao_busca import funcao_busca
from funcao_placa import funcao_placa
from cabecalhos import titulo_automarket, titulo_editar
from tkinter import messagebox

def editar(portfolio, placa):
    placa = funcao_placa(portfolio, placa)
    
    if placa:
        veiculo = funcao_busca(portfolio, placa)
        if veiculo:
            indice = portfolio.index(veiculo)
            
            def atualizar_veiculo():
                veiculo.placa = entrada_placa.get()
                veiculo.tipo = entrada_tipo.get()
                veiculo.marca = entrada_marca.get()
                veiculo.modelo = entrada_modelo.get()
                veiculo.cor = entrada_cor.get()
                veiculo.ano_fabricacao = entrada_ano.get()
                veiculo.portas = entrada_portas.get()
                veiculo.combustivel = entrada_combustivel.get()
                veiculo.conservacao = entrada_conservacao.get()
                veiculo.quilometragem = entrada_quilometragem.get()
                veiculo.preco = entrada_preco.get()
                veiculo.status = entrada_status.get()
                
                portfolio[indice] = veiculo
                messagebox.showinfo("Sucesso", "Edição realizada com sucesso!")
                app.destroy()

            # Cria uma janela modal para editar o veículo
            app = ctk.CTkToplevel()  
            app.title("Editar Veículo")
            app.geometry("400x500")

            # Frame principal com a barra de rolagem
            scroll_frame = ctk.CTkScrollableFrame(app, width=400, height=500, corner_radius=10)
            scroll_frame.pack(padx=10, pady=10, fill='both', expand=True)

            # Títulos
            titulo_automarket_frame = ctk.CTkFrame(scroll_frame)
            titulo_automarket_frame.pack(padx=20, pady=10, fill='x')
            titulo_automarket_label = ctk.CTkLabel(titulo_automarket_frame, text=titulo_automarket(), font=("Arial", 20))
            titulo_automarket_label.pack(pady=10)

            titulo_editar_frame = ctk.CTkFrame(scroll_frame)
            titulo_editar_frame.pack(padx=20, pady=10, fill='x')
            titulo_editar_label = ctk.CTkLabel(titulo_editar_frame, text=titulo_editar(), font=("Arial", 16))
            titulo_editar_label.pack(pady=10)

            # Campos de entrada com menus de opções
            def criar_entry(label_text, valor, options=None):
                ctk.CTkLabel(scroll_frame, text=label_text, font=("Arial", 14)).pack(pady=5, anchor='w')
                if options:
                    entry = ctk.CTkOptionMenu(scroll_frame, values=options)
                    entry.set(valor)
                else:
                    entry = ctk.CTkEntry(scroll_frame)
                    entry.insert(0, valor)
                entry.pack(pady=5, fill='x')
                return entry

            entrada_placa = criar_entry("Placa:", veiculo.placa)
            entrada_tipo = criar_entry("Tipo:", veiculo.tipo, ["Camioneta", "Caminhonete", "Caminhão", "Carro", "Carreta", "Motocicleta", "Outro"])
            entrada_marca = criar_entry("Marca:", veiculo.marca)
            entrada_modelo = criar_entry("Modelo:", veiculo.modelo)
            entrada_cor = criar_entry("Cor:", veiculo.cor)
            entrada_ano = criar_entry("Ano de Fabricação:", veiculo.ano_fabricacao)
            entrada_portas = criar_entry("Portas:", veiculo.portas)
            entrada_combustivel = criar_entry("Combustível:", veiculo.combustivel, ["Gasolina", "GLP", "Etanol", "GNV", "Elétrico", "Híbrido", "Outro"])
            entrada_conservacao = criar_entry("Conservação:", veiculo.conservacao, ["Novo", "Seminovo"])
            entrada_quilometragem = criar_entry("Quilometragem:", veiculo.quilometragem)
            entrada_preco = criar_entry("Preço:", veiculo.preco)
            entrada_status = criar_entry("Status:", veiculo.status, ["À venda", "Reservado", "Vendido", "Indisponível"])
            
            # Botões de confirmação e cancelamento
            ctk.CTkButton(scroll_frame, text="Confirmar", command=atualizar_veiculo).pack(pady=10)
            ctk.CTkButton(scroll_frame, text="Cancelar", command=app.destroy).pack(pady=10)
            
        else:
            # Cria uma janela modal para informar que o veículo não foi encontrado
            app = ctk.CTkToplevel()  
            app.title("Veículo Não Encontrado")
            app.geometry("400x300")

            # Frame principal com a barra de rolagem
            scroll_frame = ctk.CTkScrollableFrame(app, width=400, height=300, corner_radius=10)
            scroll_frame.pack(padx=10, pady=10, fill='both', expand=True)

            # Títulos
            titulo_automarket_frame = ctk.CTkFrame(scroll_frame)
            titulo_automarket_frame.pack(padx=20, pady=10, fill='x')
            titulo_automarket_label = ctk.CTkLabel(titulo_automarket_frame, text=titulo_automarket(), font=("Arial", 20))
            titulo_automarket_label.pack(pady=10)

            titulo_editar_frame = ctk.CTkFrame(scroll_frame)
            titulo_editar_frame.pack(padx=20, pady=10, fill='x')
            titulo_editar_label = ctk.CTkLabel(titulo_editar_frame, text=titulo_editar(), font=("Arial", 16))
            titulo_editar_label.pack(pady=10)

            # Mensagem de erro
            ctk.CTkLabel(scroll_frame, text="ERRO: Veículo não encontrado!", font=("Arial", 14)).pack(pady=10)

            # Botão de voltar
            ctk.CTkButton(scroll_frame, text="Voltar", command=app.destroy).pack(pady=10)

    else:
        messagebox.showerror("Erro", "Placa inválida!")
