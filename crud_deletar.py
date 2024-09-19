import customtkinter as ctk
import tkinter.messagebox as messagebox  # Importando o módulo messagebox do tkinter
from funcao_busca import funcao_busca
from funcao_placa import funcao_placa
from funcao_exibir import funcao_exibir
from cabecalhos import titulo_automarket, titulo_deletar
import time

def deletar(portfolio, placa):
    placa = funcao_placa(portfolio, placa)
    
    def processar_delecao():
        veiculo = funcao_busca(portfolio, placa)
        if veiculo:
            def confirmacao():
                nonlocal veiculo
                # Usar tkinter.messagebox em vez de ctk.messagebox
                if messagebox.askyesno("Confirmação", "Tem certeza que deseja deletar este veículo?"):
                    portfolio.remove(veiculo)
                    messagebox.showinfo("Sucesso", "Veículo deletado com sucesso!")
                    app.destroy()
                else:
                    app.destroy()

            # Criar detalhes do veículo usando a notação de ponto
            detalhes_veiculo = f"Modelo: {veiculo.modelo}\nPlaca: {veiculo.placa}\nAno: {veiculo.ano_fabricacao}"

            app = ctk.CTk()
            app.title("Deletar Veículo")
            app.geometry("400x300")
            
            titulo_automarket_frame = ctk.CTkFrame(app)
            titulo_automarket_frame.pack(padx=20, pady=10)
            titulo_automarket_label = ctk.CTkLabel(titulo_automarket_frame, text=titulo_automarket(), font=("Arial", 20))
            titulo_automarket_label.pack(pady=10)
            
            titulo_deletar_frame = ctk.CTkFrame(app)
            titulo_deletar_frame.pack(padx=20, pady=10)
            titulo_deletar_label = ctk.CTkLabel(titulo_deletar_frame, text=titulo_deletar(), font=("Arial", 16))
            titulo_deletar_label.pack(pady=10)
            
            funcao_exibir_frame = ctk.CTkFrame(app)
            funcao_exibir_frame.pack(padx=20, pady=10)
            ctk.CTkLabel(funcao_exibir_frame, text=detalhes_veiculo).pack()

            confirmar_button = ctk.CTkButton(app, text="Confirmar Deleção", command=confirmacao)
            confirmar_button.pack(pady=10)
            
            cancelar_button = ctk.CTkButton(app, text="Cancelar", command=app.destroy)
            cancelar_button.pack(pady=10)
            
            app.mainloop()
            
        else:
            while True:
                app = ctk.CTk()
                app.title("Veículo Não Encontrado")
                app.geometry("400x300")
                
                titulo_automarket_frame = ctk.CTkFrame(app)
                titulo_automarket_frame.pack(padx=20, pady=10)
                titulo_automarket_label = ctk.CTkLabel(titulo_automarket_frame, text=titulo_automarket(), font=("Arial", 20))
                titulo_automarket_label.pack(pady=10)
                
                titulo_deletar_frame = ctk.CTkFrame(app)
                titulo_deletar_frame.pack(padx=20, pady=10)
                titulo_deletar_label = ctk.CTkLabel(titulo_deletar_frame, text=titulo_deletar(), font=("Arial", 16))
                titulo_deletar_label.pack(pady=10)
                
                ctk.CTkLabel(app, text="ERRO: Veículo não encontrado!", font=("Arial", 14)).pack(pady=10)
                
                nova_delecao_button = ctk.CTkButton(app, text="Nova Deleção", command=lambda: (app.destroy(), deletar(portfolio, funcao_placa(portfolio, placa))))
                nova_delecao_button.pack(pady=10)
                
                voltar_menu_button = ctk.CTkButton(app, text="Voltar ao Menu", command=app.destroy)
                voltar_menu_button.pack(pady=10)
                
                app.mainloop()
                
    processar_delecao()
