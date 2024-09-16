import customtkinter as ctk
from crud_buscar import buscar
from crud_deletar import deletar
from crud_editar import editar
from crud_listar import listar
from crud_registrar import cadastrar
from persistencia import salva_banco, cria_banco
from classe_veiculo import Veiculo
from funcao_exibir import funcao_exibir
from crud_listar import listar
from crud_registrar import cadastrar
from cabecalhos import titulo_automarket, titulo_registrar

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Inicializar o portfolio com a função cria_banco
        self.portfolio = cria_banco()

        # Configurações da janela
        self.title("AutoMarket")
        self.geometry("400x300")
        self.configure(bg_color="white")

        # Configuração do layout
        self.frame = ctk.CTkFrame(self, bg_color="white")
        self.frame.pack(expand=True, fill="both")

        # Cabeçalho
        self.header = ctk.CTkLabel(self.frame, text="AutoMarket", font=("Arial", 24), bg_color="white", text_color="green")
        self.header.pack(pady=10)

        # Botões do menu
        self.btn_registrar = ctk.CTkButton(self.frame, text="Registrar Veículo", command=self.registrar_veiculo, fg_color="green", hover_color="darkgreen")
        self.btn_registrar.pack(pady=5)

        self.btn_buscar = ctk.CTkButton(self.frame, text="Buscar Veículo", command=self.buscar_veiculo, fg_color="green", hover_color="darkgreen")
        self.btn_buscar.pack(pady=5)

        self.btn_editar = ctk.CTkButton(self.frame, text="Editar Veículo", command=self.editar_veiculo, fg_color="green", hover_color="darkgreen")
        self.btn_editar.pack(pady=5)

        self.btn_listar = ctk.CTkButton(self.frame, text="Listar Portfólio", command=self.listar_veiculos, fg_color="green", hover_color="darkgreen")
        self.btn_listar.pack(pady=5)

        self.btn_deletar = ctk.CTkButton(self.frame, text="Deletar Veículo", command=self.deletar_veiculo, fg_color="green", hover_color="darkgreen")
        self.btn_deletar.pack(pady=5)

        self.btn_sair = ctk.CTkButton(self.frame, text="Sair", command=self.sair, fg_color="red", hover_color="darkred")
        self.btn_sair.pack(pady=20)

    def registrar_veiculo(self):
        cadastrar(self.portfolio)

    def buscar_veiculo(self):
        buscar(self.portfolio)

    def editar_veiculo(self):
        editar(self.portfolio)

    def listar_veiculos(self):
        listar(self.portfolio)

    def deletar_veiculo(self):
        deletar(self.portfolio)

    def sair(self):
        salva_banco(self.portfolio)  # Salvar o banco de dados antes de sair
        self.quit()

# Executar a aplicação
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
