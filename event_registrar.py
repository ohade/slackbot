from Queue import Queue


class EventRegistrar:
    def __init__(self):
        self._handlers = dict()
        self._event_queue = Queue()

    def register(self, event_type, handler):
        self._handlers[event_type] = handler

    def add_event(self, event):
        if event.type not in self._handlers:
            return
        else:
            self._event_queue.put(self._handlers[event.type](event, self))

    def get_next(self):
        return self._event_queue.get()
