class HandlerNotify:
    def __init__(self, event_info, event_registrar, members):
        self._event_info = event_info
        self._event_registrar = event_registrar
        self._members = members

    def handle(self):
        response = self._event_info.get_response()
        ## set a tracker for what the user asked
        ## maybe add an event to monitor what the user asked
        self._event_info.get_socket().api_call("chat.postMessage",
                                               channel=self._event_info.get_channel(),
                                               text=response.params["msg"],
                                               as_user=True)
