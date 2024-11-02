from services.base_service import BaseClient
from utils.request import APIRequest
from config.base import *
import json

class FirstClient(BaseClient):
    def __int__(self):
        super().__int__()
        self.base_url = BASE_URI
        self.request = APIRequest()

    def create_call(self, payload):
        url = BASE_URI
        return self.request.post_request(url, json.dumps(payload), self.headers)

    def get_call(self, booking_id):
        url = f'{BASE_URI}/{booking_id}'
        return self.request.get_request(url,self.headers)


