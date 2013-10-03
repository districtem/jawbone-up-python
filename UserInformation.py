import requests

def get_user_information(username):
	username = '@' + username
	user_information = requests.get('https://jawbone.com/nudge/api/users/username')
	return user_information

def get_user_friends(username):
	user = '@' + username
	user_friends = requests.get('https://jawbone.com/nudge/api/users/username/friends')
	return user_friends

def get_user_mood(username):
	user = '@' + username
	user_mood = requests.get('https://jawbone.com/nudge/api/users/username/mood')
	return user_mood

def get_user_trends(username):
	user = '@' + username
	user_trends = requests.get('https://jawbone.com/nudge/api/users/username/trend')
	return user_trends

# next step, create class, stand up class w/ calls


