from data.event_info import EventInfo
from data.event_type import EventType


class EventInfoGoodMorning:
    def __init__(self, bot_id, user, text, channel, socket):
        self._event_info = EventInfo(EventType.GOOD_MORNING, bot_id, user, text, channel)
        self._socket = socket

    def get_type(self):
        return self._event_info.type

    def get_user(self):
        return self._event_info.user

    def get_text(self):
        return self._event_info.text

    def get_channel(self):
        return self._event_info.channel

    def get_socket(self):
        return self._socket

    def get_bot_id(self):
        return self._event_info.bot_id

