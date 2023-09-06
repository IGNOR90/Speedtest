import requests
from bs4 import BeautifulSoup
from config import *

CONFIG = {
    'login': config['login'],
    'password': config['password'],
    'login-url': config['login-url'],
    'client-url': config['client-url']
}


class ExBillParser:
    def __init__(self):
        self.session = requests.Session()
        self.login()

    def request(self, method, url, data=None, params=None, headers=None):
        return self.session.request(method=method, url=url, data=data, params=params, headers=headers)

    def is_auth(self):
        response = self.request('GET', url=CONFIG.get('login-url'))
        if len(response.content) > 5500:
            return response
        return False

    def login(self):
        auth = self.is_auth()
        if auth:
            return auth
        login_data = {
            'login': CONFIG.get('login'),
            'password': CONFIG.get('password'),
            'do_login': 'Войти'
        }
        return self.request('POST', url=CONFIG.get('login-url'), data=login_data)

    @staticmethod
    def formParse(content):
        data = {}
        html = BeautifulSoup(content, features="lxml")
        form = html.find('form', recursive=True)
        fields = form.find_all(('input', 'select', 'textarea'))
        for field in fields:
            if not field.name:
                continue
            name = field.get('name')
            if name:
                if field.name == 'input':
                    value = field.get('value')
                    if field.get('type') == 'checkbox':
                        value = 0
                        if field.get('checked'):
                            value = 1
                elif field.name == 'select':
                    try:
                        value = field.find_all('option', selected=True)[0].get('value')
                    except:
                        value = None
                elif field.name == 'textarea':
                    value = field.text

                data[name] = value
        return data




