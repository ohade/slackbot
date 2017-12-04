import apiai
import json

from config import APIAI_CLIENT_ACCESS_TOKEN
from data.event_type import EventType
from external.action_responses.response import Response


class EventIdentifierExternal:
    def __init__(self):
        self._connector = apiai.ApiAI(APIAI_CLIENT_ACCESS_TOKEN)

    def identify(self, text):
        request = self._connector.text_request()
        request.session_id = "12345678"
        request.query = text
        response = request.getresponse()

        before_json = response.read()
        res = json.loads(before_json)
        if "smalltalk" in res["result"]["action"]:
            return EventType.SMALLTALK, Response({"msg": res["result"]["fulfillment"]["speech"]})
        if "ifttt" == res["result"]["metadata"]["intentName"]:
            action = res["result"]["parameters"]["action"]
            condition = res["result"]["parameters"]["condition"]
            return EventType.IFTTT, Response({"condition": condition, "action": action})
        if "assist" == res["result"]["metadata"]["intentName"]:
            return EventType.HELP, Response({"msg": res["result"]["fulfillment"]["messages"][0]["speech"]})
        if "input.unknown" == res["result"]["action"]:
            return EventType.OTHER, Response({"msg": res["result"]["fulfillment"]["messages"][0]["speech"]})
