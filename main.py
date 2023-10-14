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
    'api_url': 'https://panel.spi.uz/speedtest/api/'
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
    obj = {
        'client_ip': whatismyip.whatismyip()
    }
    response = requests.post(url='https://panel.spi.uz/speedtest/api/', json=obj)
    client_data = response.text
    json_object = json.loads(client_data)

    return json_object


def change_tariff(bill_user_id, tarif_id):
    obj = {}
    obj['bill_user_id'] = bill_user_id
    obj['tarif_id'] = tarif_id
    print(obj)
    req = requests.post(url='https://panel.spi.uz/speedtest/api/change_tariff', json=obj)
    print(req.text)
    return ''


def start_test():
    data = config_get()
    print(data)
    tarif_data = {}

    for a in data['tarif_lists']:
        tarif_data[a['tarif_id']] = a['tarif_name']

    for tarif_ in tarif_data:
        tarif_name = tarif_data[tarif_]
        print(tarif_, '---', tarif_name)

        oob = change_tariff(data['bill_user_id'], tarif_)
        # obj = speedtest(tarif_name)
        # send_test_data(obj)
        time.sleep(60)


def speedtest(tarif_name):
    st = Tester.Speedtest()
    setServer = find(serverList, '6386')
    st.get_best_server([setServer])
    st.set_best(setServer)
    obj = {
        'server_ping': st.results.ping,
        'server_download': round(st.download() / 1000 / 1000, 1),
        'server_upload': round(st.upload() / 1000 / 1000, 1),
        'client_ip': tarif_name
    }

    return obj


def run(sleep):
    while True:
        start_test()
        time.sleep(sleep)


if __name__ == "__main__":
    run(_config['timeout'])
