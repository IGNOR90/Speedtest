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

    for a in data['tarif_lists']:
        tarif_data[a['tariff_id']] = a['tariff_name']

    for tarif_ in tarif_data:
        tariff_name = tarif_data[tarif_]

        oob = change_tariff(data['bill_user_id'], tarif_)
        # obj = speedtest(tariff_name)
        obj = main_speed_test('tariff_name')
        print(type(obj))
        # send_test_data(obj)
        time.sleep(30)


def run(sleep):
    while True:
        start_test()
        time.sleep(sleep)


if __name__ == "__main__":
    # run(_config['timeout'])
    run(_config['timeout'])

{37382: {'type': 'result', 'timestamp': '2023-11-03T09:58:04Z', 'ping': {'jitter': 0.335, 'latency': 1.637},
         'download': {'bandwidth': 11321197, 'bytes': 43176464, 'elapsed': 3810},
         'upload': {'bandwidth': 11765193, 'bytes': 42433640, 'elapsed': 3607}, 'isp': 'SPECTR IT',
         'interface': {'internalIp': '10.34.61.110', 'name': 'enp3s0', 'macAddr': 'B4:2E:99:59:5D:9F', 'isVpn': False,
                       'externalIp': '93.170.220.67'},
         'server': {'id': 37382, 'host': 'speedtest.st.uz', 'port': 8080, 'name': 'Sharq Telekom',
                    'location': 'Tashkent', 'country': 'Uzbekistan', 'ip': '217.29.116.215'},
         'result': {'id': '1fef7e7c-6487-44ff-86a9-4c6135b02321',
                    'url': 'https://www.speedtest.net/result/c/1fef7e7c-6487-44ff-86a9-4c6135b02321',
                    'persisted': True}, 'tariff_name': 'tariff_name'}}
{37382: {'type': 'result', 'timestamp': '2023-11-03T09:58:04Z', 'ping': {'jitter': 0.335, 'latency': 1.637},
         'download': {'bandwidth': 11321197, 'bytes': 43176464, 'elapsed': 3810},
         'upload': {'bandwidth': 11765193, 'bytes': 42433640, 'elapsed': 3607}, 'isp': 'SPECTR IT',
         'interface': {'internalIp': '10.34.61.110', 'name': 'enp3s0', 'macAddr': 'B4:2E:99:59:5D:9F', 'isVpn': False,
                       'externalIp': '93.170.220.67'},
         'server': {'id': 37382, 'host': 'speedtest.st.uz', 'port': 8080, 'name': 'Sharq Telekom',
                    'location': 'Tashkent', 'country': 'Uzbekistan', 'ip': '217.29.116.215'},
         'result': {'id': '1fef7e7c-6487-44ff-86a9-4c6135b02321',
                    'url': 'https://www.speedtest.net/result/c/1fef7e7c-6487-44ff-86a9-4c6135b02321',
                    'persisted': True}, 'tariff_name': 'tariff_name'},
 46774: {'type': 'result', 'timestamp': '2023-11-03T09:58:14Z', 'ping': {'jitter': 0.128, 'latency': 1.277},
         'download': {'bandwidth': 11776572, 'bytes': 42585680, 'elapsed': 3616},
         'upload': {'bandwidth': 11766141, 'bytes': 42449568, 'elapsed': 3608}, 'packetLoss': 0, 'isp': 'SPECTR IT',
         'interface': {'internalIp': '10.34.61.110', 'name': 'enp3s0', 'macAddr': 'B4:2E:99:59:5D:9F', 'isVpn': False,
                       'externalIp': '93.170.220.67'},
         'server': {'id': 46774, 'host': 'speedtest2.uztelecom.uz', 'port': 8080, 'name': 'UZTELECOM',
                    'location': 'Tashkent', 'country': 'Uzbekistan', 'ip': '195.69.189.215'},
         'result': {'id': '43317519-3e9f-4748-ab4b-dae109de7226',
                    'url': 'https://www.speedtest.net/result/c/43317519-3e9f-4748-ab4b-dae109de7226',
                    'persisted': True}, 'tariff_name': 'tariff_name'}}
