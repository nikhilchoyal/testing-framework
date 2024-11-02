import requests
from dataclasses import dataclass
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class APIResponse:
    status_code: int
    text: str
    as_dict: object
    headers: dict


class APIRequest:

    def post_request(self, url, payload, headers):
        response = requests.post(url = url, headers= headers, data= payload)
        logger.info(f"Response Body: {response.text}")
        return self.__get_responses(response)
    def get_request(self, url, headers, params):
        response = requests.get(url=url, headers=headers, params=params)
        return self.__get_responses(response)


    @staticmethod
    def __get_responses(response):
        status_code = response.status_code
        text = response.text
        try:
            as_dict =response.json()
        except ValueError:
            as_dict = {}
        headers = response.headers
        return APIResponse(status_code, text, as_dict, headers)







