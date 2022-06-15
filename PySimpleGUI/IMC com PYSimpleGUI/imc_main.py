import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkTeal8') # Cores padrões
        # Layout
        layout = [
            [sg.Text('Nome: ', size=(5, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Peso: ', size=(5, 0)), sg.Input(size=(15, 0), key='peso')],
            [sg.Text('Altura: ', size=(5, 0)), sg.Input(size=(15, 0), key='altura')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30, 10))]
        ]


        # Janela
        self.janela = sg.Window('Dados do Usuário').layout(layout)


    def Iniciar(self):
        while True:
            #Extrair dados
            self.button, self.values = self.janela.Read()

            nome = self.values['nome']
            peso = self.values['peso']
            altura = self.values['altura']
            #resultado = eval([peso/altura**2])

            print(f'Nome: {nome}')
            print(f'Peso: {peso}')
            print(f'Altura: {altura}')
            #print(f'{resultado}')

            print('-=' * 13)        

tela = TelaPython()
tela.Iniciar()