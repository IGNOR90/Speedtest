import time
import json
import requests
from exbillparser import ExBillParser, CONFIG
import spt as Tester
from config import *


# ip = requests.get("https://api.ipify.org/?format=json").json()
file = open('serverList.json')
serverList = json.load(file)


class HttpResponse:
    pass


def send_test_data(obj):
    obj_ = json.dumps(obj)
    req = requests.post(url=config['server_url'], data=obj_)


def find(serversList, server_id):
    for server in serversList:
        if server.get('id') == server_id:
            return server
    return None

def change_tariff_name(tariff_name_id):
    parser = ExBillParser()
    getPage = parser.request('GET', url=CONFIG.get('client-url'))
    data = parser.formParse(getPage.content)
    data.update({'current_tariff_name_id': tariff_name_id})
    print(data)
    return parser.request('POST', url=CONFIG.get('client-url'), data=data)


tariff_names = {
    512: '10 Мбит',
    515: '100 Мбит'
}


def spTest(tariff_name_id):
    st = Tester.Speedtest()
    setServer = find(serverList, '6386')
    st.get_best_server([setServer])
    st.set_best(setServer)

    obj = {
        'client': config['client'],
        'server_ping': st.results.ping,
        'server_download': round(st.download() / 1000 / 1000, 1),
        'server_upload': round(st.upload() / 1000 / 1000, 1),
        'tariff_name': tariff_names.get(tariff_name_id),
        'client_ip': config['client_ip']
    }

    send_test_data(obj)
    time.sleep(5)


def run(sleep):
    while True:
        try:
            spTest(512)
            spTest(515)
        except:
            print("ERROR spTest")
        time.sleep(sleep)


if __name__ == "__main__":
    run(3600)
