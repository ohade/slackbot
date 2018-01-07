class HandlerHelp:
    def __init__(self, event_info, event_registrar, members):
        self._event_info = event_info
        self._event_registrar = event_registrar
        self._members = members

    def handle(self):
        response = self._event_info.get_response()
        self._event_info.get_socket().api_call("chat.postMessage",
                                               channel=self._event_info.get_channel(),
                                               text=response.params["msg"],
                                               as_user=True
                                               )
# testing attachments
# attachments= [
#             {
#                 "text": "Choose a game to play",
#                 "fallback": "You are unable to choose a game",
#                 "callback_id": "wopr_game",
#                 "color": "#3AA3E3",
#                 "attachment_type": "default",
#                 "actions": [
#                     {
#                         "name": "game",
#                         "text": "Chess",
#                         "type": "button",
#                         "value": "chess"
#                     },
#                     {
#                         "name": "game",
#                         "text": "Falken's Maze",
#                         "type": "button",
#                         "value": "maze"
#                     },
#                     {
#                         "name": "game",
#                         "text": "Thermonuclear War",
#                         "style": "danger",
#                         "type": "button",
#                         "value": "war",
#                         "confirm": {
#                             "title": "Are you sure?",
#                             "text": "Wouldn't you prefer a good game of chess?",
#                             "ok_text": "Yes",
#                             "dismiss_text": "No"
#                         }
#                     }
#                 ]
#             }
#         ]