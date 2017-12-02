from data.event_info import EventInfo
from data.event_type import EventType


class EventAccept:
    def __init__(self, bot_id, socket):
        self._event_info = EventInfo(EventType.ACCEPT, bot_id)
        self._socket = socket

    def get_type(self):
        return self._event_info.type

    def get_socket(self):
        return self._socket

    def get_bot_id(self):
        return self._event_info.bot_id
