import customtkinter as ctk
from crud_buscar import buscar
from crud_deletar import deletar
from crud_editar import editar
from crud_listar import listar
from crud_registrar import cadastrar
from persistencia import salva_banco, cria_banco
from classe_veiculo import Veiculo
from funcao_exibir import funcao_exibir
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
        self.header = ctk.CTkLabel(self.frame, text="AutoMarket", font=("Arial", 24, "bold"), bg_color="white", text_color="green")
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
        placa = self._obter_placa()
        if placa:
            buscar(self.portfolio, placa)

    def editar_veiculo(self):
        placa = self._obter_placa()
        if placa:
            editar(self.portfolio, placa)

    def listar_veiculos(self):
        listar(self.portfolio)

    def deletar_veiculo(self):
        placa = self._obter_placa()
        if placa:
            deletar(self.portfolio, placa)

    def sair(self):
        salva_banco(self.portfolio)  # Salvar o banco de dados antes de sair
        self.quit()

    def _obter_placa(self):
        # Criar uma nova janela para entrada de dados
        placa_window = ctk.CTkToplevel(self)
        placa_window.title("Obter Placa")
        placa_window.geometry("350x200")
        placa_window.configure(bg_color="#f5f5f5")  # Cor de fundo suave

        # Fazer a janela modal
        placa_window.transient(self)

        # Ajustar a fonte e cores para legibilidade
        lbl_prompt = ctk.CTkLabel(placa_window, text="Digite a placa do veículo:", font=("Helvetica", 16, "bold"), bg_color="#f5f5f5", text_color="#333333")
        lbl_prompt.pack(pady=(20, 10))

        placa_entry = ctk.CTkEntry(placa_window, placeholder_text="Placa", font=("Helvetica", 14), width=250, border_width=2, corner_radius=5)
        placa_entry.pack(pady=10)

        def on_ok():
            self.placa = placa_entry.get()
            placa_window.destroy()

        btn_ok = ctk.CTkButton(placa_window, text="OK", command=on_ok, fg_color="green", hover_color="darkgreen", font=("Helvetica", 14, "bold"))
        btn_ok.pack(pady=(10, 20))

        # Usa o método after para atrasar a chamada ao grab_set
        placa_window.after(10, lambda: placa_window.grab_set())

        # Esperar até a janela ser destruída
        self.wait_window(placa_window)
        return getattr(self, 'placa', None)

# Executar a aplicação
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
