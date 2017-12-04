from data.event_type import EventType
from events.event_generic import EventGeneric
from external.event_identifier import EventIdentifier
from utils import get_in_message_bot_id


class EventFactory:
    def __init__(self):
        pass

    def get_event(self, raw_event, bot_id, socket):
        clean_text = self._clean_raw_event(raw_event['text'], bot_id)
        event_type, response = EventIdentifier.identify(clean_text)
        if event_type == EventType.SMALLTALK:
            return EventGeneric(EventType.SMALLTALK,
                                bot_id,
                                raw_event['user'],
                                response,
                                raw_event['channel'],
                                socket)
        elif event_type == EventType.HELP:
            return EventGeneric(EventType.HELP,
                                bot_id,
                                raw_event['user'],
                                response,
                                raw_event['channel'],
                                socket)
        elif event_type == EventType.IFTTT:
            return EventGeneric(EventType.IFTTT,
                                bot_id,
                                raw_event['user'],
                                response,
                                raw_event['channel'],
                                socket)
        elif event_type == EventType.NOTIFY:
            return EventGeneric(EventType.NOTIFY,
                                bot_id,
                                raw_event['user'],
                                response,
                                raw_event['channel'],
                                socket)
        else:
            return EventGeneric(EventType.OTHER,
                                bot_id,
                                raw_event['user'],
                                response,
                                raw_event['channel'],
                                socket)

    @staticmethod
    def _clean_raw_event(raw_text, bot_id):
        message_bot_id = get_in_message_bot_id(bot_id)
        length_to_skip = len(message_bot_id)
        return raw_text[length_to_skip+1:]
