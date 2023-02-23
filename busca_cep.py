import requests
import json
import PySimpleGUI as sg
import pandas as pd

layout = [
    [sg.Text('Digite o cep:'), sg.InputText(key='input_cep', size=(20, 1))],
    [sg.Button('Buscar')],
]

window = sg.Window('Busca cep').Layout(layout)

event, values = window.Read()

cep_number = values['input_cep']
api_cep_url = requests.get(f'https://viacep.com.br/ws/{cep_number}/json/')
adress = json.loads(api_cep_url.text)
lista = {
    "Endereço": [
        adress['logradouro'],
        adress['bairro'],
        adress['localidade'],
        adress['uf']
    ]

}

obj = pd.json_normalize(lista)
pd.DataFrame(obj)

sg.Popup(obj)

window.close()
