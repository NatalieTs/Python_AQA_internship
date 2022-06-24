import json

import requests


class HttpClient(object):

    def __init__(self, base_url, users_path, headers):
        self.base_url = base_url
        self.headers = headers
        self.users_path = users_path

    def post(self, payload):
        response = requests.post(f"{self.base_url}{self.users_path}", headers=self.headers, data=payload)
        return self.response_loads(response)

    def put(self, prepare_user, payload):
        response = requests.put(f"{self.base_url}{self.users_path}/{prepare_user}", headers=self.headers, data=payload)
        return self.response_loads(response)

    def delete(self, user_id):
        response = requests.delete(f"{self.base_url}{self.users_path}/{user_id}", headers=self.headers)
        return self.response_loads(response)

    def get(self, prepare_user=None):
        if prepare_user is None:
            id_str = ''
        else:
            id_str = f"/{prepare_user}"
        response = requests.get(f"{self.base_url}{self.users_path}{id_str}", headers=self.headers)
        return self.response_loads(response)

    def response_loads(self, response):
        status_code = response.status_code
        try:
            body = json.loads(response.text)
        except:
            body = dict()
        return status_code, body


