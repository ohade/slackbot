class EventInfo:
    def __init__(self, event_type, bot_id=None, user=None, response=None, channel=None, person_initiating_request=None):
        self.type = event_type
        self.bot_id = bot_id
        self.user = user
        self.response = response
        self.channel = channel
        self.person_initiating_request = person_initiating_request

