import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        engineers = []

        engineers_list = json.loads(self.get_response_body())
        for engineer in engineers_list:
            engineers.append(engineer)
        return engineers