import time

from selector import Selector
from slackclient import SlackClient


class SlackBot(object):
    def __init__(self, slack_api_key):
        self._slack_client = SlackClient(slack_api_key)
        self._bot_name = "test"
        self._bot_id = self.get_bot_id()
         
        if self._bot_id is None:
            exit("Error, could not find " + self._bot_name)

        self.selector = Selector(self._slack_client, self._bot_id)
        self.listen()
     
    def get_bot_id(self):
        api_call = self._slack_client.api_call("users.list")
        if api_call.get('ok'):
            # retrieve all users so we can find our bot
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == self._bot_name:
                    return "<@" + user.get('id') + ">"
             
            return None
             
    def listen(self):
        if self._slack_client.rtm_connect(with_team_state=False):
            print "Successfully connected, listening for commands"
            while True:
                self.selector.select()
                 
                time.sleep(1)
        else:
            exit("Error, Connection Failed")
