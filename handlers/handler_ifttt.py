class HandlerIFTTT:
    def __init__(self, event_info, event_registrar, members):
        self._event_info = event_info
        self._event_registrar = event_registrar
        self._members = members

    def handle(self):
        response = self._event_info.get_response()
        text = "Do: {}, After: {}".format(response.params["action"], response.params["condition"])
        self._event_info.get_socket().api_call("chat.postMessage",
                                               channel=self._event_info.get_channel(),
                                               text=text,
                                               as_user=True)
