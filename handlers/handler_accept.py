from events.event_factory import EventFactory
from utils import get_in_message_bot_id


class HandlerAccept:
    def __init__(self, event_info, event_registrar):
        self._event_info = event_info
        self._event_registrar = event_registrar
        self._event_factory = EventFactory()

    def handle(self):
        socket = self._event_info.get_socket()
        raw_events = socket.rtm_read()

        if raw_events and len(raw_events) > 0:
            for raw_event in raw_events:
                if raw_event['type'] != "message" or raw_event['user'] == self._event_info.get_bot_id():
                    continue
                event = self._parse_event(raw_event)
                if event:
                    self._event_registrar.add_event(event)

        # we register the event again to allow us to read the socket again once all the event we read this time
        # are done
        self._event_registrar.add_event(self._event_info)

    def _parse_event(self, raw_event):
        bot_id = self._event_info.get_bot_id()
        if raw_event and 'text' in raw_event and (
                    get_in_message_bot_id(bot_id) in raw_event['text'] or
                    ("channel" in raw_event and
                         self._event_info.is_member_of_channel(raw_event["channel"])
                     )):
            return self._event_factory.get_event(raw_event, bot_id, self._event_info.get_socket())
        else:
            print "Can't parse event", raw_event
            return None
