import customtkinter
from tkinter import filedialog
from tkinter.messagebox import showinfo
from pathlib import Path

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x215")
        #self.minsize(400,215)
        #self.maxsize(400,215)
        self.title("Exportador de Esocial")
        self.file_path = ''

        # add widgets to app
        self.label_arquivo = customtkinter.CTkLabel(self, text="Insira o ARQUIVO:")
        self.button_arquivo = customtkinter.CTkButton(self, text="Importar Arquivo", command=self.import_data_button_click)
        self.label_arquivo_selecionado = customtkinter.CTkLabel(self, text="")
        self.label_chapa = customtkinter.CTkLabel(self, text="Insira a CHAPA:")
        self.entry_chapa = customtkinter.CTkEntry(self, placeholder_text="Ex: 0045 ou 0006")
        self.label_evento = customtkinter.CTkLabel(self, text="Insira o EVENTO:")
        self.entry_evento = customtkinter.CTkEntry(self, placeholder_text="Ex: S2200 ou S2206")
        self.button = customtkinter.CTkButton(self, text="Exportar Arquivo ", command=self.export_data_button_click)

        self.label_arquivo.grid(row=0, column=0, padx=20, pady=5)
        self.button_arquivo.grid(row=1, column=0, padx=20, pady=5)
        self.label_arquivo_selecionado.grid(row=1, column=1, padx=20, pady=(0,5))
        self.label_chapa.grid(row=2, column=0, padx=20, pady=(0,5))
        self.entry_chapa.grid(row=3, column=0, padx=20, pady=(0,5))
        self.label_evento.grid(row=4, column=0, padx=20, pady=(0,5))
        self.entry_evento.grid(row=5, column=0, padx=20, pady=(0,5))
        self.button.grid(row=5, column=1, padx=20, pady=(0,5))

    # add methods to app
    def export_data_button_click(self):
        self.export_file_path = filedialog.asksaveasfilename(
            initialfile="arquivo_modificado.txt",
            filetypes=[("Text files", ".txt"), ("All files", "*.*")]
        )
        chapa_alvo = self.entry_chapa.get()
        evento_alvo = self.entry_evento.get()
        self.alterar_linha_no_arquivo(self.file_path, self.export_file_path, chapa_alvo, evento_alvo)

    def import_data_button_click(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Text files", ".txt"), ("All files", "*.*")]
        )
        if self.file_path:
            path = Path(self.file_path)
            self.label_arquivo_selecionado.configure(text=path.name)
        else:
            showinfo(
                title="Aviso",
                message="Nenhum arquivo selecionado."
            )
    
    def alterar_linha_no_arquivo(self, input_file, output_file, chapa_alvo, evento_alvo):
        try:
            with open(input_file, 'r', encoding='latin-1') as file:
                linhas = file.readlines()
        except UnicodeDecodeError:
            with open(input_file, 'r', encoding='utf-8') as file:
                linhas = file.readlines()

        linhas_modificadas = []
        for linha in linhas:
            chapa = linha[14:18]   # Colunas 17 e 18 (índices 16 e 17)
            evento = linha[22:27]  # Colunas 23 e 24 (índices 22 e 23)
            numero = linha[195:197] # Colunas 196 e 197 (índices 195 e 196)
            print(f'LINHA: {linha}')
            print(f'CHAPA: {chapa}')
            print(f'EVENTO: {evento}')
            if chapa == chapa_alvo and evento == evento_alvo:
                # Substitui o número nas colunas 196/197 por "2"
                print("BATEU")
                linha = linha[:195] + '2' + linha[196:]

            linhas_modificadas.append(linha)

        # Salva o arquivo modificado
        with open(output_file, 'w') as file:
            file.writelines(linhas_modificadas)



app = App()
app.mainloop()

