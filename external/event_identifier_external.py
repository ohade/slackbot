import apiai
import json

from config import APIAI_CLIENT_ACCESS_TOKEN
from external.action_responses.ifttt import IFTTT
from external.action_responses.input_unknown import InputUnknown
from external.action_responses.smalltalk import Smalltalk


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
            return Smalltalk(res["result"]["fulfillment"]["speech"])
        if "input.unknown" == res["result"]["action"]:
            return InputUnknown(res["result"]["fulfillment"]["messages"][0]["speech"])
        if "ifttt" == res["result"]["metadata"]["intentName"]:
            action = res["result"]["parameters"]["action"]
            condition = res["result"]["parameters"]["condition"]
            return IFTTT(condition=condition, action=action)
