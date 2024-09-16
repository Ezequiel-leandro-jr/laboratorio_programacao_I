import customtkinter as ctk
from funcao_busca import funcao_busca
from funcao_placa import funcao_placa
from classe_veiculo import Veiculo
from funcao_exibir import funcao_exibir
from cabecalhos import titulo_automarket, titulo_editar
import time

def editar(portfolio, placa):
    placa = funcao_placa(portfolio, placa)

    def editar_veiculo(veiculo, indice):
        def atualizar_veiculo(campo, valor):
            setattr(veiculo, campo, valor)
            portfolio[indice] = veiculo
            ctk.messagebox.showinfo("Sucesso", "Edição realizada com sucesso!")
            app.destroy()

        def selecionar_campo():
            def opcao_selecionada():
                campo = {
                    '1': 'placa',
                    '2': 'tipo',
                    '3': 'marca',
                    '4': 'modelo',
                    '5': 'cor',
                    '6': 'ano_fabricacao',
                    '7': 'portas',
                    '8': 'combustivel',
                    '9': 'conservacao',
                    '10': 'quilometragem',
                    '11': 'preco',
                    '12': 'status'
                }.get(campo_selecionado.get(), None)
                
                if campo:
                    valor = entrada.get()
                    atualizar_veiculo(campo, valor)
                else:
                    ctk.messagebox.showerror("Erro", "Opção inválida!")
                
            app = ctk.CTk()
            app.title("Editar Veículo")
            app.geometry("400x300")

            titulo_automarket_frame = ctk.CTkFrame(app)
            titulo_automarket_frame.pack(padx=20, pady=10)
            titulo_automarket_label = ctk.CTkLabel(titulo_automarket_frame, text=titulo_automarket(), font=("Arial", 20))
            titulo_automarket_label.pack(pady=10)

            titulo_editar_frame = ctk.CTkFrame(app)
            titulo_editar_frame.pack(padx=20, pady=10)
            titulo_editar_label = ctk.CTkLabel(titulo_editar_frame, text=titulo_editar(), font=("Arial", 16))
            titulo_editar_label.pack(pady=10)

            ctk.CTkLabel(app, text="Selecione o campo a ser editado:", font=("Arial", 14)).pack(pady=10)
            campo_selecionado = ctk.StringVar()
            ctk.CTkOptionMenu(app, values=[
                "1. Placa", "2. Tipo", "3. Marca", "4. Modelo", "5. Cor", 
                "6. Ano de fabricação", "7. Portas", "8. Combustível", 
                "9. Conservação", "10. Quilometragem", "11. Preço", "12. Status"], 
                variable=campo_selecionado
            ).pack(pady=10)

            entrada = ctk.CTkEntry(app)
            entrada.pack(pady=10)
            
            ctk.CTkButton(app, text="Confirmar", command=opcao_selecionada).pack(pady=10)
            ctk.CTkButton(app, text="Cancelar", command=app.destroy).pack(pady=10)

            app.mainloop()

    veiculo = funcao_busca(portfolio, placa)
    if veiculo:
        indice = portfolio.index(veiculo)
        
        def exibir_opcoes():
            def opcao_escolhida():
                escolha = opcao_selecionada.get()
                if escolha == '1':
                    editar_veiculo(veiculo, indice)
                elif escolha == '2':
                    placa = input_placa.get()
                    if placa:
                        editar(portfolio, placa)
                    app.destroy()
                elif escolha == '3':
                    app.destroy()
                else:
                    ctk.messagebox.showerror("Erro", "Opção inválida!")
            
            app = ctk.CTk()
            app.title("Escolha a Ação")
            app.geometry("400x300")

            titulo_automarket_frame = ctk.CTkFrame(app)
            titulo_automarket_frame.pack(padx=20, pady=10)
            titulo_automarket_label = ctk.CTkLabel(titulo_automarket_frame, text=titulo_automarket(), font=("Arial", 20))
            titulo_automarket_label.pack(pady=10)

            titulo_editar_frame = ctk.CTkFrame(app)
            titulo_editar_frame.pack(padx=20, pady=10)
            titulo_editar_label = ctk.CTkLabel(titulo_editar_frame, text=titulo_editar(), font=("Arial", 16))
            titulo_editar_label.pack(pady=10)

            ctk.CTkLabel(app, text="Escolha o que deseja fazer:", font=("Arial", 14)).pack(pady=10)
            opcao_selecionada = ctk.StringVar()
            ctk.CTkOptionMenu(app, values=[
                "1. Continuar Edição", 
                "2. Editar Outro Veículo", 
                "3. Voltar ao Menu"], 
                variable=opcao_selecionada
            ).pack(pady=10)

            input_placa = ctk.CTkEntry(app)
            input_placa.pack(pady=10)

            ctk.CTkButton(app, text="Confirmar", command=opcao_escolhida).pack(pady=10)
            ctk.CTkButton(app, text="Cancelar", command=app.destroy).pack(pady=10)

            app.mainloop()

    else:
        def veiculo_nao_encontrado():
            def acao_escolhida():
                escolha = opcao_selecionada.get()
                if escolha == '1':
                    placa = input_placa.get()
                    if placa:
                        editar(portfolio, placa)
                    app.destroy()
                elif escolha == '2':
                    app.destroy()
                else:
                    ctk.messagebox.showerror("Erro", "Opção inválida!")

            app = ctk.CTk()
            app.title("Veículo Não Encontrado")
            app.geometry("400x300")

            titulo_automarket_frame = ctk.CTkFrame(app)
            titulo_automarket_frame.pack(padx=20, pady=10)
            titulo_automarket_label = ctk.CTkLabel(titulo_automarket_frame, text=titulo_automarket(), font=("Arial", 20))
            titulo_automarket_label.pack(pady=10)

            titulo_editar_frame = ctk.CTkFrame(app)
            titulo_editar_frame.pack(padx=20, pady=10)
            titulo_editar_label = ctk.CTkLabel(titulo_editar_frame, text=titulo_editar(), font=("Arial", 16))
            titulo_editar_label.pack(pady=10)

            ctk.CTkLabel(app, text="ERRO: Veículo não encontrado!", font=("Arial", 14)).pack(pady=10)

            ctk.CTkLabel(app, text="Escolha o que deseja fazer:", font=("Arial", 14)).pack(pady=10)
            opcao_selecionada = ctk.StringVar()
            ctk.CTkOptionMenu(app, values=[
                "1. Editar Novo Veículo",
                "2. Voltar ao Menu"],
                variable=opcao_selecionada
            ).pack(pady=10)

            input_placa = ctk.CTkEntry(app)
            input_placa.pack(pady=10)

            ctk.CTkButton(app, text="Confirmar", command=acao_escolhida).pack(pady=10)
            ctk.CTkButton(app, text="Cancelar", command=app.destroy).pack(pady=10)

            app.mainloop()
