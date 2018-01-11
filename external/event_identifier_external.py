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
        params = {"msg": res["result"]["fulfillment"]["messages"][0]["speech"]}

        if "smalltalk" in res["result"]["action"]:
            return EventType.SMALLTALK, Response(params)
        if "ifttt" == res["result"]["metadata"]["intentName"]:
            return EventType.IFTTT, Response(res["result"]["parameters"])
        if "assist" == res["result"]["metadata"]["intentName"]:
            return EventType.HELP, Response(params)
        if "notify" == res["result"]["metadata"]["intentName"]:
            params.update(res["result"]["parameters"])
            return EventType.NOTIFY, Response(params)
        if "register" == res["result"]["metadata"]["intentName"]:
            params.update(res["result"]["parameters"])
            return EventType.REGISTER, Response(params)
        if "input.unknown" == res["result"]["action"]:
            return EventType.OTHER, Response(params)
