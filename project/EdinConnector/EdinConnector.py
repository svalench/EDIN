import json

import requests
from suds.client import Client
from .constants import METHODS, ERRORS_TEXT
from .settings import settings
import xmltodict


class EDiNConnector:
    """Базовый класс для подключения к системе ЭДиН и обмена сообщениями"""

    def __init__(self):
        self.request_timeout = 60 if not settings.request_timeout else settings.request_timeout
        self.url = settings.wsdl_url
        self.client = Client(self.url)

    async def send_soap_request(self, method, data):
        response = self.client.service.ListDocuments(**dict(data))
        print(response)
        print(response.Content)
        print(dir(response))
        result = json.dumps(xmltodict.parse(response.Content))
        return result

    def send_request(self, postfix: str, type_request: str, data: dict) -> dict:
        type_request = type_request.upper()
        if type_request not in METHODS:
            return {'status': False, 'error': ERRORS_TEXT['BAD_METHOD']}
        if postfix[0] == '/':
            return {'status': False, 'error': ERRORS_TEXT['BAD_PREFIX']}
        request = requests.Session()
        headers = {'content-type': 'text/xml'}
        response = request.request(
            url=settings.wsdl_url+postfix,
            method=type_request,
            data=data,
            headers=headers
        )
        if response.status_code in [301, 302, 404]:
            return {'status': False, 'error': ERRORS_TEXT['BAD_PREFIX']}
        if response.status_code not in [404] and response.status_code > 400:
            return {'status': False, 'error': ERRORS_TEXT['BAD_REQUEST'] % response.status_code}
        if response.status_code not in [200, 201, 202]:
            return {'status': False, 'error': ERRORS_TEXT['BAD_REQUEST'] % response.status_code}
        try:
            result = response.json()
        except Exception as e:
            return {'status': False, 'error': ERRORS_TEXT['BAD_REQUEST'] % str(e)}