import requests

def get_user_information(username):
	username = '@' + username
	user_information = requests.get(https://jawbone.com/nudge/api/users/username)
	return user_information

def get_users_friends(username):
	user = '@' + username
	users_friends = requests.get(https://jawbone.com/nudge/api/users/username/friends)
	return users_friends


# next step, create class, stand up class w/ calls