from data.event_info import EventInfo


class EventInfoAccept:
    def __init__(self, event_type, socket, bot_id):
        self._event_info = EventInfo(event_type)
        self._socket = socket
        self._bot_id = bot_id

    def get_type(self):
        return self._event_info.type

    def get_socket(self):
        return self._socket

    def get_bot_id(self):
        return self._bot_id
