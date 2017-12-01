

class HandlerGoodMorning:
    def __init__(self, event_info, event_registrar):
        self._event_info = event_info
        self._event_registrar = event_registrar

    def handle(self):
        self._event_info.get_socket().api_call("chat.postMessage",
                                               channel=self._event_info.get_channel(),
                                               text="Good morning to you too",
                                               as_user=True)
