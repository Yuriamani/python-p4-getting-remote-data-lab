import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        responce = requests.get(self.url)
        return responce.content

    def load_json(self):
        doc = GetRequester.get_response_body(self)
        return json.loads(doc)
   