import requests
import random
from frase_otaku import gerar_frase_otaku
from api_data import headers, cookies
import datetime as dt


class Bot:
    def __init__(self):
        pass


def entrar_na_sala(id_sala):
    params = {
        'id': id_sala,
    }

    requests.get('https://drrr.com/room/', params=params, cookies=cookies, headers=headers)


def gerar_frase_aleatoria():
    response = requests.get('https://moraislucas.github.io/MeMotive/phrases.json')

    num = random.randint(0, 288)
    print(f'num: {num}')

    print(response)
    return response.json()[num]['quote']


def sair_da_sala():
    params = {
        'ajax': '1',
    }

    data = {
        'message': '/leave',
        'loudness': '3',
    }

    response = requests.post('https://drrr.com/room/', params=params, cookies=cookies, headers=headers, data=data)
    print(response)


def mandar_mensagem_motivacional():
    params = {
        'ajax': '1',
    }

    data = {
        'message': 'BOT - FRASE MOTIVACIONAL: ' + gerar_frase_aleatoria(),
        'loudness': '3',
    }
    response = requests.post('https://drrr.com/room/', params=params, cookies=cookies, headers=headers, data=data)
    print(response)


def mandar_mensagem_otaku():
    params = {
        'ajax': '1',
    }

    data = {
        'message': 'BOT: ' + gerar_frase_otaku(),
        'loudness': '1',
    }
    response = requests.post('https://drrr.com/room/', params=params, cookies=cookies, headers=headers, data=data)
    print(response)


def ver_status():
    response = requests.get('https://drrr.com/room/?api=json', cookies=cookies, headers=headers)
    dicionario = response.json()
    keys = str(dicionario.keys())
    if 'redirect' and 'message' and 'authorization' in keys:
        return False
    else:
        return True


def pegar_ultima_msg():
    response = requests.get('https://drrr.com/room/?api=json', cookies=cookies, headers=headers)
    lista_recente = response.json()['room']['talks'][0]
    timestamp = lista_recente['time']

    tempo_utc = dt.datetime.fromtimestamp(timestamp, dt.UTC)
    tempo_br = tempo_utc - dt.timedelta(hours=3)
    print(response, dt.datetime.now().strftime("%H:%M:%S"))

    return tempo_br


def ver_intervalo(intervalo: int):
    intervalo = dt.timedelta(minutes=intervalo)

    agora = dt.datetime.now()
    agora = agora - intervalo

    return agora.strftime("%H:%M")


def leave():
    data = {
        'message': '/leave',
    }
    params = {
        'ajax': '1',
    }
    requests.post('https://drrr.com/room/', params=params, cookies=cookies, headers=headers, data=data)


def setar_tempo_limite(intervalo):
    tempo_limite = (pegar_ultima_msg() + intervalo).strftime("%H:%M")
    return tempo_limite
