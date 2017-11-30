class EventInfo:
    def __init__(self, event_type, user=None, text=None, channel=None):
        self._type = event_type
        self.user = user
        self.text = text
        self.channel = channel

    def get_type(self):
        return self._type