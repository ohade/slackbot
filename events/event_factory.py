from data.event_identifier import EventIdentifier
from data.event_type import EventType
from events.event_good_morning import EventGoodMorning
from events.event_help import EventHelp
from events.event_other import EventOther


class EventFactory:
    def __init__(self):
        pass

    def get_event(self, raw_event, bot_id, socket):
        event_type = EventIdentifier.identify(raw_event['text'])
        if event_type == EventType.GOOD_MORNING:
            return EventGoodMorning(bot_id,
                                    raw_event['user'],
                                    raw_event['text'].split(bot_id)[1].strip().lower(),
                                    raw_event['channel'],
                                    socket)
        elif event_type == EventType.HELP:
            return EventHelp(bot_id,
                             raw_event['user'],
                             raw_event['text'].split(bot_id)[1].strip().lower(),
                             raw_event['channel'],
                             socket)
        else:
            return EventOther(bot_id,
                              raw_event['user'],
                              raw_event['text'].split(bot_id)[1].strip().lower(),
                              raw_event['channel'],
                              socket)
