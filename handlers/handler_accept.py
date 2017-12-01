from data.event_identifier import EventIdentifier
from data.event_info import EventInfo
from data.event_info_good_morning import EventInfoGoodMorning
from data.event_info_other import EventInfoOther
from data.event_type import EventType
from utils import get_in_message_bot_id


class HandlerAccept:
    def __init__(self, event_info, event_registrar):
        self._event_info = event_info
        self._event_registrar = event_registrar

    def handle(self):
        socket = self._event_info.get_socket()
        events = socket.rtm_read()

        if events and len(events) > 0:
            for event in events:
                if event['type'] != "message" or event['user'] == self._event_info.get_bot_id():
                    continue
                event = self._parse_event(event)
                if event:
                    self._event_registrar.add_event(event)

        # we register the event again to allow us to read the socket again once all the event we read this time
        # are done
        self._event_registrar.add_event(self._event_info)

    def _parse_event(self, event):
        bot_id = self._event_info.get_bot_id()
        if event and 'text' in event and get_in_message_bot_id(bot_id) in event['text']:
            event_type = EventIdentifier.identify(event['text'])
            if event_type == EventType.GOOD_MORNING:
                return EventInfoGoodMorning(self._event_info.get_bot_id(),
                                            event['user'],
                                            event['text'].split(bot_id)[1].strip().lower(),
                                            event['channel'],
                                            self._event_info.get_socket())
            else:
                return EventInfoOther(self._event_info.get_bot_id(),
                                      event['user'],
                                      event['text'].split(bot_id)[1].strip().lower(),
                                      event['channel'],
                                      self._event_info.get_socket())
        else:
            print "Can't parse event", event
            return None
