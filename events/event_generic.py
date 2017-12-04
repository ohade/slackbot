from data.event_info import EventInfo


class EventGeneric:
    def __init__(self, event_type, bot_id, user, response, channel, socket):
        self._event_info = EventInfo(event_type, bot_id, user, response, channel)
        self._socket = socket

    def get_type(self):
        return self._event_info.type

    def get_user(self):
        return self._event_info.user

    def get_response(self):
        return self._event_info.response

    def get_channel(self):
        return self._event_info.channel

    def get_socket(self):
        return self._socket

    def get_bot_id(self):
        return self._event_info.bot_id

