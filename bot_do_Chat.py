import requests
from weeb_quote import generate_weeb_quote
import datetime as dt


class Bot:
    def __init__(self, cookies, headers, params):
        self.cookies = cookies
        self.headers = headers
        self.params = params

    def join_room(self, room_id):
        params = {'id': room_id}
        requests.get('https://drrr.com/room/', params=params, cookies=self.cookies, headers=self.headers)

    def send_weeb_quote(self):
        data = {
            'message': '|BOT| ' + generate_weeb_quote(),
            'loudness': '1',
        }
        response = requests.post('https://drrr.com/room/', params=self.params, cookies=self.cookies,
                                 headers=self.headers, data=data)
        print(response)

    def see_status(self):
        response = requests.get('https://drrr.com/room/?api=json', cookies=self.cookies, headers=self.headers)
        dicionario = response.json()
        keys = str(dicionario.keys())
        if 'redirect' and 'message' and 'authorization' in keys:
            return False
        else:
            return True

    def get_last_message(self):
        response = requests.get('https://drrr.com/room/?api=json', cookies=self.cookies, headers=self.headers)
        lista_recente = response.json()['room']['talks'][0]
        timestamp = lista_recente['time']

        tempo_utc = dt.datetime.fromtimestamp(timestamp, dt.UTC)
        tempo_br = tempo_utc - dt.timedelta(hours=3)
        print(response, dt.datetime.now().strftime("%H:%M:%S"))

        return tempo_br

    @staticmethod
    def set_timelimit(bot, gap):
        tempo_limite = (bot.get_last_message() + gap).strftime("%H:%M")
        return tempo_limite

    def leave_room(self):

        data = {
            'message': '/leave',
            'loudness': '3',
        }

        response = requests.post('https://drrr.com/room/', params=self.params, cookies=self.cookies,
                                 headers=self.headers,
                                 data=data)
        print(response)
