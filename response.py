import requests
import json

from requests.exceptions import RequestException


class Endpoint:
    def __init__(self):
        with open("endpoints.json", "r") as file:
            self.apis = json.load(file)
    def test(self):
        for api in self.apis:
            try:
                get = requests.get(api, timeout=5)
                if get.status_code == 200:
                    print(f"[ONLINE]  {api} ")
                else:
                    print(f"[HTTP {get.status_code}] {api} ")
            except requests.RequestException:
                print(f"[OFFLINE] {api} ")
       
main = Endpoint()
main.test()
