import requests
import json

from requests.exceptions import RequestException


class Endpoint:
    def __init__(self):
        with open("endpoints.json", "r") as file:
            self.apis = json.load(file)
    def test(self):
        for name, url in self.apis.items():
            try:
                get = requests.get(url, timeout=5)
                if get.status_code == 200:
                    print(f"[ONLINE]  {name}: {url} ")
                else:
                    print(f"[HTTP {get.status_code}] {name}: {url} ")
            except requests.RequestException:
                print(f"[OFFLINE] {url} ")
       
main = Endpoint()
main.test()
