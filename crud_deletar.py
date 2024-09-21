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
            app.geometry("500x400")

            # Criar um frame para os detalhes do veículo
            detalhes_frame = ctk.CTkFrame(app)
            detalhes_frame.pack(padx=20, pady=10, fill='both', expand=True)

            # Adicionar a descrição do veículo de forma estilizada
            ctk.CTkLabel(detalhes_frame, text="DETALHES DO VEÍCULO", font=("Helvetica", 16, "bold"), text_color="#1C1C1C").pack(pady=5)

            ctk.CTkLabel(detalhes_frame, text=f"PLACA: {veiculo.placa}  |  TIPO: {veiculo.tipo}  |  MARCA: {veiculo.marca}  |  MODELO: {veiculo.modelo}", 
                         font=("Helvetica", 12), text_color="#333333").pack(pady=2)

            ctk.CTkLabel(detalhes_frame, text=f"ANO: {veiculo.ano_fabricacao}  |  COR: {veiculo.cor}  |  PORTAS: {veiculo.portas}  |  COMBUSTÍVEL: {veiculo.combustivel}", 
                         font=("Helvetica", 12), text_color="#333333").pack(pady=2)

            ctk.CTkLabel(detalhes_frame, text=f"ESTADO: {veiculo.conservacao}  |  KM: {veiculo.quilometragem:.2f} Km  |  PREÇO: R${veiculo.preco}", 
                         font=("Helvetica", 12), text_color="#333333").pack(pady=2)

            ctk.CTkLabel(detalhes_frame, text=f"STATUS: {veiculo.status}", 
                         font=("Helvetica", 12, "italic"), text_color="#1C1C1C").pack(pady=2)

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
            app.geometry("400x300")

            # Criar um frame para a mensagem de erro
            erro_frame = ctk.CTkFrame(app)
            erro_frame.pack(padx=20, pady=10, fill='both', expand=True)
            
            ctk.CTkLabel(erro_frame, text="ERRO: Veículo não encontrado!", font=("Helvetica", 14)).pack(pady=10)

            botoes_frame = ctk.CTkFrame(app)
            botoes_frame.pack(pady=10)
            
            voltar_menu_button = ctk.CTkButton(botoes_frame, text="Voltar ao Menu", command=app.destroy)
            voltar_menu_button.pack(side='left', padx=10)

            
            app.mainloop()

    processar_delecao()