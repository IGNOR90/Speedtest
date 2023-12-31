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
    print(data)
    if len(data['tarif_lists']) >= 2:
        for a in data['tarif_lists']:
            tarif_data[a['tariff_id']] = a['tariff_name']
        for tarif_ in tarif_data:
            tariff_name = tarif_data[tarif_]
            oob = change_tariff(data['bill_user_id'], tarif_)
            obj = main_speed_test(tariff_name)
            data_r = {}
            for k in obj:
                data_r[k] = obj[k]
                obj_k = obj[k]
                obj_k['bill_user_id'] = data['bill_user_id']

                send_test_data(obj[k])
                print(f"-------------------------{obj[k]['server']['name']}-------------------------------------", obj[k], "--------------------------------------------------------------")

            time.sleep(30)
    else:
        obj = main_speed_test('0')
        data_r = {}
        for k in obj:
            data_r[k] = obj[k]
            obj_k = obj[k]
            obj_k['bill_user_id'] = data['bill_user_id']

            send_test_data(obj[k])
            print(f"-------------------------{obj[k]['server']['name']}-------------------------------------", obj[k],
                  "--------------------------------------------------------------")

        time.sleep(30)


def run(sleep):
    while True:
        start_test()
        time.sleep(sleep)


if __name__ == "__main__":
    # run(_config['timeout'])
    run(_config['timeout'])
