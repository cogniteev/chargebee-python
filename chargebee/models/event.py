import json

from chargebee.model import Model
from chargebee import request
from chargebee import APIError


class Event(Model):

    @property
    def content(self):
        from chargebee import Content
        return Content(self.values['content'])

    @staticmethod
    def deserialize(json_data):
        try:
            webhook_data = json.loads(json_data)
        except (TypeError, ValueError):
            raise APIError("Invalid webhook object to deserialize")

        return Event.construct(webhook_data)

    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/events', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/events/%s' % id, None, env)
