import bot_do_Chat as bC
import datetime as dt
from time import sleep
from json import JSONDecodeError

id_sala = 'MaiHL6MycT'

if __name__ == '__main__':
    intervalo = dt.timedelta(minutes=15)
    try:
        bC.setar_tempo_limite(intervalo)
    except KeyError:
        bC.entrar_na_sala(id_sala)
        sleep(1)
        bC.setar_tempo_limite(intervalo)

    while True:
        sleep(2)
        try:
            if bC.ver_status():
                try:
                    tempo_limite = bC.setar_tempo_limite(intervalo)
                    print(f'tempo limite: {tempo_limite}')
                    if int(tempo_limite.replace(":", "")) <= int(dt.datetime.now().strftime("%H:%M").replace(":", "")):
                        print(f'o tempo limite foi batido: {tempo_limite}')
                        bC.mandar_mensagem_otaku()
                        sleep(1)
                        tempo_limite = bC.setar_tempo_limite(intervalo)
                        print(f'Novo tempo limite: {tempo_limite}')
                except KeyError:
                    bC.entrar_na_sala(id_sala)
                except JSONDecodeError:
                    print("A resposta não contém um JSON válido.")
            else:
                bC.entrar_na_sala(id_sala)
        except JSONDecodeError:
            print("A resposta não contém um JSON válido.")
