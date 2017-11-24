class EventInfo:
    def __init__(self, event_type, user=None, text=None, channel=None):
        self.type = event_type
        self.user = user
        self.text = text
        self.channel = channel
