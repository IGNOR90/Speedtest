import time
import json
import requests
import whatismyip
import spt as Tester
from test import main_speed_test

# ip = requests.get("https://api.ipify.org/?format=json").json()
file = open('serverList.json')
serverList = json.load(file)

_config = {
    'timeout': 3600,
    'api_url': 'https://panel.spi.uz/speedtest/api/',
    'client_ip': whatismyip.whatismyip()
}


class HttpResponse:
    pass


def send_test_data(obj):
    obj_ = json.dumps(obj)
    req = requests.post(url=_config['api_url'], data=obj_)


def find(serversList, server_id):
    for server in serversList:
        if server.get('id') == server_id:
            return server
    return None


def config_get():
    obj = {}
    obj['client_ip'] = _config['client_ip']
    response = requests.post(url='https://panel.spi.uz/speedtest/api/config', json=obj)
    client_data = response.text
    json_object = json.loads(client_data)

    return json_object


def change_tariff(bill_user_id, tariff_id):
    obj = {}
    obj['bill_user_id'] = bill_user_id
    obj['tariff_id'] = tariff_id
    req = requests.post(url='https://panel.spi.uz/speedtest/api/change_tariff', json=obj)
    return ''


def start_test():
    data = config_get()
    tarif_data = {}
    obj = {}

    for a in data['tarif_lists']:
        tarif_data[a['tariff_id']] = a['tariff_name']

    for tarif_ in tarif_data:
        tariff_name = tarif_data[tarif_]

        oob = change_tariff(data['bill_user_id'], tarif_)
        obj = main_speed_test(tariff_name)
        print('1 ')
        print(obj)
        send_test_data(obj)
        print('2')
        time.sleep(30)


def run(sleep):
    while True:
        start_test()
        time.sleep(sleep)


if __name__ == "__main__":
    # run(_config['timeout'])
    run(_config['timeout'])

