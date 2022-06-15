import PySimpleGUI as sg      

layout = [
    [sg.Text('Nome: ', size=(7, 0)), sg.Input(size=(15, 0), key='nome')],
    [sg.Text('Peso: ', size=(7, 0)), sg.Input(size=(15, 0), key='peso')],
    [sg.Text('Altura: ', size=(7, 0)), sg.Input(size=(15, 0), key='altura')],
    [sg.Submit(), sg.Cancel()]

]

window = sg.Window('IMC', layout)    

event, values = window.read()    
window.close()

nome = values['nome']
peso = float(values['peso'])
altura = float(values['altura'])
imc = peso/altura**2

'''
if imc < 18.5: 
    print('Você está abaixo do peso.')
elif imc > 18.5 and imc < 24.9:
    print('Você está no peso normal - Eutrofia')
elif imc > 25 and imc < 29.9:
    print('Acima do peso - Sobre peso, pré-obesidade')
elif imc > 30 and imc < 34.9:
    print('Obesidade I - Moderada')
elif imc > 35 and imc < 39.9:
    print('Obesidade II - Severa')
else:
    print('Obesidade III - Muito Severa')
'''    

sg.popup('Seu IMC', f'{str(nome.title())}, seu peso de {str(peso)} com altura de {str(altura)} possui um IMC de: {float(imc):.2f}.')

