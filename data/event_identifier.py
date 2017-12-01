from data.event_type import EventType


class EventIdentifier:
    event_to_phrases = {EventType.GOOD_MORNING: ["good morning", "morning"]}

    def __init__(self):
        pass

    @classmethod
    def identify(cls, text):
        for event_type, phrases in cls.event_to_phrases.iteritems():
            for phrase in phrases:
                if phrase in text.lower():
                    return event_type
        return EventType.OTHER
