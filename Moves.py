import requests

from UserInformation import UserRequests

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

