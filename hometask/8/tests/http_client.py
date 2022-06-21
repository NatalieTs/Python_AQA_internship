import requests


class HttpClient(object):

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def post(self, path, payload):
        return requests.post(f"{self.base_url}{path}", headers=self.headers, data=payload)

    def put(self, path, payload):
        return requests.put(f"{self.base_url}{path}", headers=self.headers, data=payload)

    def delete(self, path):
        return requests.delete(f"{self.base_url}{path}", headers=self.headers)

    def get(self, path):
        return requests.get(f"{self.base_url}{path}", headers=self.headers)

