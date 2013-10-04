import requests

# USER INFORMATION
class UserRequests(object):
	def __init__(self, username):
		self.username = '@' + username
		self.user_information = None
		self.user_mood = None
		self.user_trends = None

	@property
	def user_request_url_base(self):
		return 'https://jawbone.com/nudge/api/v.1.0/users/%s' % self.username

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

# MOVES
def get_user_moves(user):
	user = UserRequests(username=user)
	user_api_url = user.user_request_url_base
	user_moves = requests.get(user_api_url + '/moves')
	return user_moves

def get_specific_move(move_xid):
	move_id = move_xid
	return requests.get('https://jawbone.com/nudge/api/v.1.0/moves/{%s}' % move_id)

def get_move_graphs(move_xid):
	move_id = move_xid
	return requests.get('https://jawbone.com/nudge/api/v.1.0/moves/{%s}/image' % move_id)

def get_move_intensity(move_xid):
	move_id = move_xid
	return requests.get('https://jawbone.come/nudge/api/v.1.0/moves/{%s}/snapshot')	


#  WORKOUTS
def get_user_workouts(user):
	user = UserRequests(username=user)
	user_api_url = user.user_request_url_base
	user_workouts = requests.get(user_api_url + '/workouts')
	return user_workouts

def get_specific_workout(workout_xid):
	workout_id = workout_xid
	return requests.get('https://jawbone.com/nudge/api/v.1.0/workouts/{%s}' % workout_id)

def get_user_workout_graphs(workout_xid):
	workout_id = workout_xid
	return requests.get('https://jawbone.com/nudge/api/v.1.0/workouts/{%s}/image' % workout_id)

def get_workout_intensity(workout_xid):
	workout_id = workout_xid
	return requests.get('https://jawbone.com/nudge/api/v.1.0/workouts/{%s}/snapshot' % workout_id)

def create_new_workout():
	pass



