import time
from data.event_info import EventInfo
from event_type import EventType


class HandlerAccept:
    def __init__(self, event_info, event_registrar):
        self._event_info = event_info
        self._event_registrar = event_registrar

    def handle(self):
        socket = self._event_info.get_socket()
        events = socket.rtm_read()

        if events and len(events) > 0:
            for event in events:
                if event['type'] != "message":
                    continue
                print "Got event", event
                event = self._parse_event(event)
                if event:
                    self._event_registrar.add_event(event)

        # we register the event again to allow us to read the socket again once all the event we read this time
        # are done
        self._event_registrar.add_event(self._event_info)

    def _parse_event(self, event):
        bot_id = self._event_info.get_bot_id()
        print bot_id, bot_id in event['text']
        if event and 'text' in event and bot_id in event['text']:
            self._event_info.get_socket().api_call("chat.postMessage", channel=event['channel'], text="Good morning", as_user=True)
            return EventInfo(EventType.OTHER,
                             event['user'],
                             event['text'].split(bot_id)[1].strip().lower(),
                             event['channel'])
        else:
            print "Can't parse event", event
            return None
