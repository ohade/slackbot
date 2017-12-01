from Queue import Queue

from data.event_type import EventType


class EventRegistrar:
    def __init__(self):
        self._event_type_to_handlers = dict()
        self._event_queue = Queue()

    def register(self, event_type, handler):
        self._event_type_to_handlers[event_type] = handler

    def add_event(self, event):
        if event.get_type() not in self._event_type_to_handlers:
            print "can't handle this event!!!", event.get_type()
            return
        else:
            self._event_queue.put(self._event_type_to_handlers[event.get_type()](event, self))

    def get_next(self):
        return self._event_queue.get()
