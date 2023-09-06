import json

import requests


def findServer(str=''):
    uri = 'https://www.speedtest.net/api/js/servers?engine=js&search=' + str + '&https_functional=true&limit=999'
    response = requests.get(uri)
    return response.json()


def getList():
    alf = ['a', 'b', 'moscow']
    lists = []
    for a in alf:
        lists += findServer(a)
    return json.dumps(lists)


def cleanList():
    file = open('trash/servers.json')
    data = json.load(file)
    ok = []
    ok_ids = []
    for i in data:
        if i.get('id') not in ok_ids:
            ok.append(i)
            ok_ids.append(i.get('id'))
