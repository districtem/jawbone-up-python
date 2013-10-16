import requests


class Client(object):
    def __init__(self, authorization_token):
        self.username = '@me'
        self.token = authorization_token
        self.auth_header = {'Authorization': 'Bearer %s' % self.token}
        self.version = 'v.1.0/'
        self.api_url_base = 'https://jawbone.com/nudge/api/%s/' % self.version, 

    # USER REQUESTS
    @property
    def user_request_url_base(self):
        return 'https://jawbone.com/nudge/api/v.1.0/users/%s' % self.username

    def get_user_information(self):
        user_information_request = requests.get(self.user_request_url_base, headers=self.auth_header)
        return user_information.json

    def get_user_friends(self):
        user_friends_request = requests.get(self.user_request_url_base + '/friends', headers=self.auth_header)
        return user_friends_reqeust.json

    def get_user_mood(self):
        user_mood_request = requests.get(self.user_request_url_base + '/mood', headers=self.auth_header)
        return user_mood_request.json

    def get_user_trends(self):
        user_trends_request = requests.get(self.user_request_url_base + '/trend', headers=self.auth_header)
        return user_trends_request.json

    def get_user_moves(self):
        user_moves_request = requests.get(self.user_request_url_base + '/moves', headers=self.auth_header)
        return user_moves_request.json

    def get_user_workouts(self):
        user_workouts_request = requests.get(self.user_request_url_base + '/workouts', headers=self.auth_header)
        return user_workouts_request.json

        # MOVES
    def get_specific_move(self, move_xid):
        move_id = move_xid
        specific_move_request = requests.get(self.api_url_base +  '%s/%s' % ('moves',  move_id), headers=self.auth_header)
        return specific_move_request.json

    def get_move_graphs(self, move_xid):
        move_id = move_xid
        move_graphs_request = requests.get(self.api_url_base + '%s/%s/%s' % ('moves',  move_id, 'image'), headers=self.auth_header)
        return move_graphs.json

    def get_move_intensity(self, move_xid):
        move_id = move_xid
        move_intensity_request = requests.get(self.api_url_base + '%s/%s/%s' % ('moves',  move_id, 'snapshot'), headers=self.auth_header)   
        return move_intensity.json

    #  WORKOUTS
    def get_specific_workout(self, workout_xid):
        workout_id = workout_xid
        specific_workout_request = requests.get(self.api_url_base+  '%s/%s' % ('workouts',  workout_id), headers=self.auth_header)
        return specific_workout.json

    def get_user_workout_graphs(self, workout_xid):
        workout_id = workout_xid
        workout_graphs_request = requests.get(self.api_url_base + '%s/%s/%s' % ('workouts',  workout_id, 'image'), headers=self.auth_header)
        return workout_graphs.json

    def get_workout_intensity(self, workout_xid):
        workout_id = workout_xid
        workout_intensity_request = requests.get(self.api_url_base + '%s/%s/%s' % ('workouts',  workout_id, 'snapshot'), headers=self.auth_header)
        return workout_intensity.json





