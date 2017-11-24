from data.event_info_accept import EventInfoAccept
from event_registrar import EventRegistrar
from event_type import EventType

from handlers.handler_accept import HandlerAccept


class Selector:
    def __init__(self, socket, bot_id):
        self._socket = socket
        self._event_registrar = EventRegistrar()
        self._event_registrar.register(EventType.ACCEPT, HandlerAccept)
        self._event_registrar.add_event(EventInfoAccept(EventType.ACCEPT, socket, bot_id))

    def select(self):
        while True:
            runner = self._event_registrar.get_next()
            runner.handle()
