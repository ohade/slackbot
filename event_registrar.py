from Queue import Queue
import datetime

from event_registrar_item import EventRegistrarItem


class EventRegistrar:
    def __init__(self, members):
        self._event_type_to_handlers = dict()
        self._event_queue = list()
        self._members = members

    def register(self, event_type, handler):
        self._event_type_to_handlers[event_type] = handler

    # TODO: need to work on the start, interval and repeat, and then
    # i won't need to support adding the event "accept" each time
    # also i need this to support the nagging of the bot
    def add_event(self, event, start=None, interval=None, repeat=False):
        if not start:
            start = datetime.datetime.now()

        if event.get_type() not in self._event_type_to_handlers:
            print "can't handle this event!!!", event.get_type()
            return
        else:
            handler = self._event_type_to_handlers[event.get_type()](event, self, self._members)
            item = EventRegistrarItem(handler, start, interval, repeat)
            self._event_queue.append(item)

    def get_next(self):
        if self._event_queue:
            item = self._event_queue[0]
            del self._event_queue[0]
            if item.repeat:
                self._event_queue.append(item)
            return item.handler
        return None
