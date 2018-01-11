import apiai
import json

from config import APIAI_CLIENT_ACCESS_TOKEN


def simple_test():
    ai = apiai.ApiAI(APIAI_CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    # request.lang = 'de'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    request.query = "booga booga"
    # request.query = "hello"
    response = request.getresponse()

    # print response.read()
    # print type(response.read())
    print type(response)
    res = json.loads(response.read())
    print res["result"]["metadata"]["intentName"]
    print res["result"]["fulfillment"]["speech"]


def ifttt_test():
    ai = apiai.ApiAI(APIAI_CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    # request.lang = 'de'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    # request.query = "do that great action after this beautiful action finishes"
    # request.query = "hello"
    request.query = "let me know when the test passes"
    response = request.getresponse()

    # print response.read()
    # print type(response.read())
    print type(response)
    before_json = response.read()
    res = json.loads(before_json)
    print before_json
    print res["result"]["metadata"]["intentName"]
    print res["result"]["parameters"]
    print res["result"]["fulfillment"]["messages"][0]["speech"]

    # if "smalltalk" in res["result"]["action"]:
    #     print "smalltalk", res["result"]["fulfillment"]["speech"]
    # elif "input.unknown" == res["result"]["action"]:
    #     print "input.unknown"
    #     print before_json
    #     print res["result"]["fulfillment"]["messages"][0]["speech"]
    # else:
    #     print res["result"]["metadata"]["intentName"] == "ifttt"
    #     print "Action:", res["result"]["parameters"]["action"]
    #     print "Condition:", res["result"]["parameters"]["condition"]
    #     print before_json


if __name__ == '__main__':
    ifttt_test()
#
# after that action finishes do that action
# do that when that finishes
# when that finish then do that
# if that finished then do that
# if i want to do that then make me do the other thing first

#do that when that finishes