import customtkinter
from tkinter import filedialog

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x175")
        self.title("Exportador de Esocial")

        # add widgets to app
        self.label_chapa = customtkinter.CTkLabel(self, text="Insira a CHAPA:")
        self.entry_chapa = customtkinter.CTkEntry(self, placeholder_text="Ex: 0045 ou 0006")
        self.label_evento = customtkinter.CTkLabel(self, text="Insira o EVENTO:")
        self.entry_evento = customtkinter.CTkEntry(self, placeholder_text="Ex: S2200 ou S2206")
        self.button = customtkinter.CTkButton(self, text="Resetar Eventos ", command=self.button_click)

        self.label_chapa.grid(row=0, column=0, padx=20, pady=5)
        self.entry_chapa.grid(row=1, column=0, padx=20, pady=(0,5))
        self.label_evento.grid(row=2, column=0, padx=20, pady=(0,5))
        self.entry_evento.grid(row=3, column=0, padx=20, pady=(0,5))
        self.button.grid(row=3, column=1, padx=20, pady=(0,5))

    # add methods to app
    def button_click(self):
        input_file = self.input_data_button_click()
        output_file = 'arquivo_modificado.txt'
        chapa_alvo = self.entry_chapa.get()
        evento_alvo = self.entry_evento.get()
        self.alterar_linha_no_arquivo(input_file, output_file, chapa_alvo, evento_alvo)

    def input_data_button_click(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", ".txt"), ("All files", "*.*")]
        )
        return file_path
    
    def alterar_linha_no_arquivo(self, input_file, output_file, chapa_alvo, evento_alvo):
        with open(input_file, 'r') as file:
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

