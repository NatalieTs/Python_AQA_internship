import requests


class HttpClient(object):

    def __init__(self, base_url, users_path, headers):
        self.base_url = base_url
        self.headers = headers
        self.users_path = users_path

    def post(self, payload):
        return requests.post(f"{self.base_url}{self.users_path}", headers=self.headers, data=payload)

    def put(self, prepare_user, payload):
        return requests.put(f"{self.base_url}{self.users_path}/{prepare_user}", headers=self.headers, data=payload)

    def delete(self, user_id):
        return requests.delete(f"{self.base_url}{self.users_path}/{user_id}", headers=self.headers)

    def get(self, prepare_user=None):
        if prepare_user == None:
            id_str = ''
        else:
            id_str = f"/{prepare_user}"
        return requests.get(f"{self.base_url}{self.users_path}{id_str}", headers=self.headers)

