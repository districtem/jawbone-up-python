import requests

class Client(object):

	def __init__(self, authorization_token):
		self.token = authorization_token
		self.auth_header = {'Authorization': 'Bearer %s' % self.token}


class JawboneAPI(object):

	def __init__(self, Client):
		self.version = 'v.1.0/'
		self.api_url_base = 'https://jawbone.com/nudge/api/%s/' % self.version
		self.header = Client.auth_header



	 
	
