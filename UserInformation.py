import requests


class UserRequests(object):
	def __init__(self, username):
		self.username = '@' + username
		self.user_information = None
		self.user_mood = None
		self.user_trends = None

	@property
	def user_request_url_base(self):
		return 'https://jawbone.com/nudge/api/users/%s' % self.username

	def get_user_information(self):
		user_information = requests.get(self.user_request_url_base)
		return user_information

	def get_user_friends(self):
		user_friends = requests.get(self.user_request_url_base + '/friends')
		return user_friends

	def get_user_mood(self):
		user_mood = requests.get(self.user_request_url_base + '/mood')
		return user_mood

	def get_user_trends(self):
		user_trends = requests.get(self.user_request_url_base + '/trend')
		return user_trends


