from data.event_info_accept import EventInfoAccept
from data.event_type import EventType
from event_registrar import EventRegistrar
from handlers.handler_accept import HandlerAccept
from handlers.handler_good_morning import HandlerGoodMorning
from handlers.handler_other import HandlerOther


class Selector:
    def __init__(self, socket, bot_id):
        self._event_registrar = EventRegistrar()
        self._event_registrar.register(EventType.ACCEPT, HandlerAccept)
        self._event_registrar.register(EventType.GOOD_MORNING, HandlerGoodMorning)
        self._event_registrar.register(EventType.OTHER, HandlerOther)
        self._event_registrar.add_event(EventInfoAccept(bot_id, socket))

    def select(self):
        while True:
            runner = self._event_registrar.get_next()
            runner.handle()
