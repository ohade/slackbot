from event_registrar import EventRegistrar


class Selector:
    def __init__(self, members):
        self._event_registrar = EventRegistrar(members)

    def select(self):
        return self._event_registrar.get_next()

    def get_event_registrar(self):
        return self._event_registrar
