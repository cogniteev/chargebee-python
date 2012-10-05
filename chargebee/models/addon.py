from chargebee.model import Model
from chargebee import request


class Addon(Model):

    def list(self, params=None, env=None):
        return request.send('get', '/addons', params, env)

    def retrieve(self, id, env=None):
        return request.send('get', '/addons/%s' % id, {}, env)
