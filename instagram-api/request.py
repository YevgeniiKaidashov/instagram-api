import requests
import json
from enum import Enum
from .exceptions import InvalidRequestType


class RequestType(Enum):
    post = 1
    get = 2


class RequestManager(object):

    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, url, data=None):
        data = data or {}
        return self._make_request(url, RequestType.post, data)

    def get(self, url, params=None):
        params = params or {}
        return self._make_request(url, RequestType.get, params)

    def _prepare_url(self, url):
        return '{}/{}'.format(self.base_url.rstrip('/'), url.lstrip('/'))

    def _make_request(self, url, request_type, data):
        request_url = self._prepare_url(url=url)

        if request_type == RequestType.get:
            response = requests.get(request_url, params=data)
        elif request_type == RequestType.post:
            response = requests.post(request_url, data=data)
        else:
            raise InvalidRequestType('Unsupported request type ({})'.format(request_type))

        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print("Request return " + str(response.status_code) + " error.")
