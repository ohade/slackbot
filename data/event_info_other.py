from data.event_info import EventInfo
from data.event_type import EventType


class EventInfoOther:
    def __init__(self, bot_id, user, text, channel, socket):
        self._event_info = EventInfo(EventType.OTHER, bot_id, user, text, channel)
        self._socket = socket

    def get_type(self):
        return self._event_info.type

    def get_text(self):
        return self._event_info.text

    def get_channel(self):
        return self._event_info.channel

    def get_bot_id(self):
        return self._event_info.bot_id

    def get_socket(self):
        return self._socket
