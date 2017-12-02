import apiai
import json

from config import APIAI_CLIENT_ACCESS_TOKEN


def main():
    ai = apiai.ApiAI(APIAI_CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'de'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    request.query = "do you know anything?"
    # request.query = "hello"
    response = request.getresponse()

    # print response.read()
    # print type(response.read())
    print type(response)
    res = json.loads(response.read())
    print res["result"]["metadata"]["intentName"]
    print res["result"]["fulfillment"]["speech"]


if __name__ == '__main__':
    main()
