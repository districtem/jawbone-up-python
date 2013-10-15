import requests


class Client(object):
    def __init__(self, authorization_token):
        self.username = '@me'
        self.token = authorization_token
        self.auth_header = {'Authorization': 'Bearer %s' % self.token}
        self.version = 'v.1.0/'
        self.api_url_base = 'https://jawbone.com/nudge/api/%s/' % self.version

    @property
    def user_request_url_base(self):
        return 'https://jawbone.com/nudge/api/v.1.0/users/%s' % self.username

    def get_user_information(self):
        user_information = requests.get(self.user_request_url_base, headers=self.auth_header)
        return user_information.json



