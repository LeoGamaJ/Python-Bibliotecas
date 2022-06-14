import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('Dark2') # Cores padrões
        # Layout
        layout = [
            [sg.Text('Nome: ', size=(5, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Idade: ', size=(5, 0)), sg.Input(size=(15, 0), key='idade')],
            [sg.Text('Quais provedores de e-mails são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartões', key='aceitaCartao'), sg.Radio('Não', 'cartões', key='naoAceitaCartao')],
            [sg.Slider(range=(0, 255), default_value=0, orientation='h', size=(15, 20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30, 20))]
        ]

        # Janela
        self.janela = sg.Window('Dados do Usuário').layout(layout)
        


    def Iniciar(self):
        while True:
            #Extrair dados
            self.button, self.values = self.janela.Read()

            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['idade']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita gmail: {aceita_gmail}')
            print(f'Aceita outlook: {aceita_outlook}')
            print(f'Aceita yahoo: {aceita_yahoo}')
            print(f'Aceita cartão: {aceita_cartao}')
            print(f'Não aceita cartão: {nao_aceita_cartao}')
            print(f'Velocidade do Script: {nome}')
            print('-=' * 13)    


tela = TelaPython()
tela.Iniciar()