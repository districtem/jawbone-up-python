import requests

from UserInformation import UserRequests


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