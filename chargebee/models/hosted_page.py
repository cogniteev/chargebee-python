from chargebee.model import Model
from chargebee import request


class HostedPage(Model):

    @property
    def content(self):
        from chargebee import Content
        return Content(self.values['content'])

    @staticmethod
    def checkout_new(params, env=None):
        return request.send('post', '/hosted_pages/checkout_new', params, env)

    @staticmethod
    def checkout_existing(params, env=None):
        return request.send('post', '/hosted_pages/checkout_existing', params, env)

    @staticmethod
    def update_card(params, env=None):
        return request.send('post', '/hosted_pages/update_card', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/hosted_pages/%s' % id, None, env)
