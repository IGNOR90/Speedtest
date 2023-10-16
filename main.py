import time
import json
import requests
import whatismyip
import spt as Tester

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
    print('-----1', response)
    client_data = response.text
    print('-----2', client_data)
    json_object = json.loads(client_data)
    print('-----3', json_object)

    return json_object


def change_tariff(bill_user_id, tariff_id):
    obj = {}
    obj['bill_user_id'] = bill_user_id
    obj['tariff_id'] = tariff_id
    print(obj)
    req = requests.post(url='https://panel.spi.uz/speedtest/api/change_tariff', json=obj)
    print(req.text)
    return ''


def start_test():
    data = config_get()
    print(data)
    tarif_data = {}

    for a in data['tarif_lists']:
        tarif_data[a['tariff_id']] = a['tariff_name']

    for tarif_ in tarif_data:
        tariff_name = tarif_data[tarif_]
        print(tarif_, '---', tariff_name)

        oob = change_tariff(data['bill_user_id'], tarif_)
        obj = speedtest(tariff_name)
        send_test_data(obj)
        time.sleep(30)


def speedtest(tariff_name):
    st = Tester.Speedtest()
    setServer = find(serverList, '6386')
    st.get_best_server([setServer])
    st.set_best(setServer)
    obj = {
        'server_ping': st.results.ping,
        'server_download': round(st.download() / 1000 / 1000, 1),
        'server_upload': round(st.upload() / 1000 / 1000, 1),
        'tariff_name': tariff_name,
        'client_ip': _config['client_ip'],
    }

    print(obj)

    return obj


def run(sleep):
    while True:
        start_test()
        time.sleep(sleep)


if __name__ == "__main__":
    run(_config['timeout'])
