class HandlerDeploy:
    def __init__(self, event_info, event_registrar):
        self._event_info = event_info
        self._event_registrar = event_registrar

    def handle(self):
        env_name = self._event_info.get_env_name()
        version_name = self._event_info.version_name()

        response = self._event_info.get_response()
        self._event_info.get_socket().api_call("chat.postMessage",
                                               channel=self._event_info.get_channel(),
                                               text="Deploying Version: {}, on Env: {}".format(version_name, env_name),
                                               as_user=True
                                               )