from data.event_type import EventType
from events.event_generic import EventGeneric
from external.event_identifier import EventIdentifier
from utils import get_in_message_bot_id
from functools import partial


class EventFactory:
    def __init__(self):
        self._type_to_event = dict()
        self._type_to_event[EventType.SMALLTALK] = partial(self._build_event, event_type=EventType.SMALLTALK)
        self._type_to_event[EventType.HELP] = partial(self._build_event, event_type=EventType.HELP)
        self._type_to_event[EventType.IFTTT] = partial(self._build_event, event_type=EventType.IFTTT)
        self._type_to_event[EventType.REGISTER] = partial(self._build_event, event_type=EventType.REGISTER)
        self._type_to_event[EventType.OTHER] = partial(self._build_event, event_type=EventType.OTHER)

    def get_event(self, raw_event, bot_id, socket):
        clean_text = self._clean_raw_event(raw_event['text'], bot_id)
        event_type, response = EventIdentifier.identify(clean_text)
        print "In EventFactory, Channel:", raw_event['channel'], raw_event['user']
        print event_type
        if event_type not in self._type_to_event:
            return self._type_to_event[EventType.OTHER](bot_id, raw_event, response, socket, raw_event['user'])
        else:
            return self._type_to_event[event_type](bot_id, raw_event, response, socket, raw_event['user'])

    @staticmethod
    def _clean_raw_event(raw_text, bot_id):
        message_bot_id = get_in_message_bot_id(bot_id)
        length_to_skip = len(message_bot_id)
        if message_bot_id in raw_text:
            return raw_text[length_to_skip+1:]
        else:
            return raw_text

    def _build_event(self, bot_id, raw_event, response, socket, person_initiating_request, event_type):
        return EventGeneric(event_type,
                            bot_id,
                            raw_event['user'],
                            response,
                            raw_event['channel'],
                            socket,
                            person_initiating_request)
