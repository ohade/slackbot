class EventInfo:
    def __init__(self, event_type, bot_id=None, user=None, text=None, channel=None):
        self.type = event_type
        self.bot_id = bot_id
        self.user = user
        self.text = text
        self.channel = channel
