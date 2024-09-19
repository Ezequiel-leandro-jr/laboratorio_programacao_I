import customtkinter as ctk
import tkinter.messagebox as messagebox  # Importando o módulo messagebox do tkinter
from funcao_busca import funcao_busca
from funcao_placa import funcao_placa
from cabecalhos import titulo_automarket, titulo_deletar

def deletar(portfolio, placa):
    placa = funcao_placa(portfolio, placa)
    
    def processar_delecao():
        veiculo = funcao_busca(portfolio, placa)
        if veiculo:
            def confirmacao():
                nonlocal veiculo
                if messagebox.askyesno("Confirmação", "Tem certeza que deseja deletar este veículo?"):
                    portfolio.remove(veiculo)
                    messagebox.showinfo("Sucesso", "Veículo deletado com sucesso!")
                app.destroy()

            app = ctk.CTk()
            app.title("Deletar Veículo")
            
            # Ajustar a geometria da janela com base no conteúdo
            app.update_idletasks()  # Atualiza o layout para ajustar o tamanho da janela
            largura = 400
            altura = 300
            app.geometry(f"{largura}x{altura}")

            # Criar um frame para os detalhes do veículo
            detalhes_frame = ctk.CTkFrame(app)
            detalhes_frame.pack(padx=20, pady=10, fill='both', expand=True)

            # Exibir detalhes do veículo de forma personalizada
            ctk.CTkLabel(detalhes_frame, text=f"Modelo: {veiculo.modelo}", font=("Arial", 14)).pack(anchor='w', pady=2)
            ctk.CTkLabel(detalhes_frame, text=f"Placa: {veiculo.placa}", font=("Arial", 14)).pack(anchor='w', pady=2)
            ctk.CTkLabel(detalhes_frame, text=f"Ano: {veiculo.ano_fabricacao}", font=("Arial", 14)).pack(anchor='w', pady=2)

            # Adicionar botões para confirmar ou cancelar
            botoes_frame = ctk.CTkFrame(app)
            botoes_frame.pack(pady=10)

            confirmar_button = ctk.CTkButton(botoes_frame, text="Confirmar Deleção", command=confirmacao)
            confirmar_button.pack(side='left', padx=10)

            cancelar_button = ctk.CTkButton(botoes_frame, text="Cancelar", command=app.destroy)
            cancelar_button.pack(side='left', padx=10)
            
            app.mainloop()
            
        else:
            app = ctk.CTk()
            app.title("Veículo Não Encontrado")
            
            # Ajustar a geometria da janela com base no conteúdo
            app.update_idletasks()
            largura = 400
            altura = 300
            app.geometry(f"{largura}x{altura}")

            # Criar um frame para a mensagem de erro
            erro_frame = ctk.CTkFrame(app)
            erro_frame.pack(padx=20, pady=10, fill='both', expand=True)
            
            ctk.CTkLabel(erro_frame, text="ERRO: Veículo não encontrado!", font=("Arial", 14)).pack(pady=10)

            botoes_frame = ctk.CTkFrame(app)
            botoes_frame.pack(pady=10)

            nova_delecao_button = ctk.CTkButton(botoes_frame, text="Nova Deleção", command=lambda: (app.destroy(), deletar(portfolio, funcao_placa(portfolio, placa))))
            nova_delecao_button.pack(side='left', padx=10)
            
            voltar_menu_button = ctk.CTkButton(botoes_frame, text="Voltar ao Menu", command=app.destroy)
            voltar_menu_button.pack(side='left', padx=10)

            app.mainloop()

    processar_delecao()
