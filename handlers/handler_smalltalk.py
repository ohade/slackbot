class HandlerSmalltalk:
    def __init__(self, event_info, event_registrar):
        self._event_info = event_info
        self._event_registrar = event_registrar

    def handle(self):
        response = self._event_info.get_response()
        self._event_info.get_socket().api_call("chat.postMessage",
                                               channel=self._event_info.get_channel(),
                                               text=response.params["msg"],
                                               as_user=True)
