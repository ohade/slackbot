from data.event_type import EventType
from external.event_identifier_external import EventIdentifierExternal


class EventIdentifier:
    # event_to_phrases = {
    #     EventType.GOOD_MORNING: ["good morning", "morning"],
    #     EventType.HELP: ["what can you do", "help", "show me what you know"]
    # }

    def __init__(self):
        pass

    @classmethod
    def identify(cls, text):
        external_identifier = EventIdentifierExternal()
        result = external_identifier.identify(text)
        print "in EventIdentifierExternal, user sent:", text, "response is:", result
        return result

        # for event_type, phrases in cls.event_to_phrases.iteritems():
        #     for phrase in phrases:
        #         if phrase in text.lower():
        #             return event_type
        # return EventType.OTHER
