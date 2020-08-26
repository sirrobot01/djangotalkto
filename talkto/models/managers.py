from typing import Dict

from django.conf import settings
from django.core.exceptions import (
    FieldDoesNotExist, )
from django.db import models
from httpx import Client

try:
    config = settings.TALKTO.get('default')
except:
    raise ValueError('You need to set create a Dict TALKTO with its values. Check the documentation')


BASE_URL = config.get('URL', None)
if not BASE_URL:
    raise ValueError("Dict TALKTO  missing a non-optional item 'URL' ")
headers = config.get('HEADERS', {})
if not BASE_URL.startswith('http'):
    raise ValueError('You need to add protocol to your URL parameter')
_client = Client(base_url=BASE_URL, headers=headers)


class APIManager(models.Manager):
    def __init__(self, path: str):
        if path.startswith('/') and BASE_URL.endswith('/'):
            self.path = path.lstrip('/')
        elif not path.startswith('/') and not BASE_URL.endswith('/'):
            self.path = '/' + path
        else:
            self.path = path
        self.client = _client
        self.model = None
        self.name = None

    def fields(self):
        return [f.name for f in self.model._meta.fields]

    def all(self):
        resp = self.client.get(url=self.path)

        return resp

    def get(self, path: str = None, **params):
        fields = self.fields()
        for param in params.keys():
            if param not in fields:
                raise FieldDoesNotExist(f"Cannot resolve keyword {param} into field. Choices are:{', '.join(fields)}")
        if not path:
            resp = self.client.get(url=self.path, params=params)
        else:
            resp = self.client.get(url=path, params=params)
        return resp

    def create(self, path: str = None, data: Dict = None):
        fields = self.fields()
        for param in data.keys():
            if param not in fields:
                raise FieldDoesNotExist(f"Cannot resolve keyword {param} into field. Choices are:{', '.join(fields)}")
        if not path:
            resp = self.client.post(url=self.path, json=data)
        else:
            resp = self.client.post(url=path, json=data)
        return resp

    def update(self, path: str = None, data: Dict = None):
        fields = self.fields()
        for param in data.keys():
            if param not in fields:
                raise FieldDoesNotExist(f"Cannot resolve keyword {param} into field. Choices are:{', '.join(fields)}")
        if not path:
            resp = self.client.put(url=self.path, json=data)
        else:
            resp = self.client.put(url=path, json=data)
        return resp

    def filter(self):
        pass
