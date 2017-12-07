from data.event_info import EventInfo
from data.event_type import EventType


class EventAccept:
    def __init__(self, bot_id, socket, channel_bot_is_member, im_bot_is_member):
        self._event_info = EventInfo(EventType.ACCEPT, bot_id)
        self._socket = socket
        self._channel_bot_is_member = channel_bot_is_member
        self._im_bot_is_member = im_bot_is_member

    def get_type(self):
        return self._event_info.type

    def get_socket(self):
        return self._socket

    def get_bot_id(self):
        return self._event_info.bot_id

    def is_member_of_channel(self, channel_id):
        return self.is_member_of_public_channel(channel_id) or self.is_member_of_im(channel_id)

    def is_member_of_public_channel(self, channel_id):
        return channel_id in self._channel_bot_is_member

    def is_member_of_im(self, channel_id):
        return channel_id in self._im_bot_is_member

    def get_other_member_of_im(self, channel_id):
        return self._im_bot_is_member[channel_id]
