from .request import RequestManager


class InstagramApi(object):
    host = 'https://api.instagram.com/v1'

    class ApiUrl(object):
        user_info = '/users/self'
        user_media = '/users/self/media/recent'

    def __init__(self, access_token=None):
        self.url = self.ApiUrl()
        self.request_manager = RequestManager(base_url=self.host)
        self.access_token = access_token

    def get_user_info(self):
        return self.request_manager.get(url=self.url.user_info, params=self._prepare_data())

    def get_user_media(self, data=None):
        return self.request_manager.get(url=self.url.user_media, params=self._prepare_data(data))

    def _prepare_data(self, data=None):
        data = data or {}
        data['access_token'] = self.access_token
        return data
