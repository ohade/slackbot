from slackclient import SlackClient

from config import SLACKBOT_CLIENT_ACCESS_TOKEN
from config import SLACKBOT_CLIENT_NAME
from data.event_type import EventType
from events.event_accept import EventAccept
from handlers.handler_accept import HandlerAccept
from handlers.handler_ifttt import HandlerIFTTT
from handlers.handler_notify import HandlerNotify
from handlers.handler_register import HandlerRegister
from handlers.handler_smalltalk import HandlerSmalltalk
from handlers.handler_help import HandlerHelp
from handlers.handler_other import HandlerOther
from selector import Selector


class SlackBot(object):
    def __init__(self, slack_api_key):
        self._slack_client = SlackClient(slack_api_key)
        self._bot_name = SLACKBOT_CLIENT_NAME
        self._bot_id = None
        self._members = dict()
        self._channel_bot_is_member = dict()
        self._im_bot_is_member = dict()

        self._get_members_info()

        if self._bot_id is None:
            exit("Error, could not find " + self._bot_name)
        self._selector = Selector(self._members)
        self._register_event()

    def _get_members_info(self):
        api_call = self._slack_client.api_call("users.list")
        im_info = self._slack_client.api_call("im.list")
        groups_info = self._slack_client.api_call("groups.list")
        all_groups_info = self._slack_client.api_call("channels.list")
        for group in all_groups_info['channels']:

            if group['name_normalized'] == 'rnd-updates':
                print group['num_members'], group['members']
                # self._slack_client.api_call("chat.postMessage",
                #                             channel=o['id'],
                #                             text="<!channel> Hey guys, i am here to remind you that the biweekly pub show is in a 6 days!!! :scream:\n Try to think about intresting things to talk about. If you need any \"person of intrest\" from other groups to attend, please invite them.\n\n On a personal note i plan to get better and to be here to suggest to you what to talk about in the future, and to help in any way i can :grinning:",
                #                             as_user=True
                #                             )
                print "rnd-updates id is:", group['id']

        for im in im_info['ims']:
            self._im_bot_is_member[im['id']] = im['user']

        if api_call.get('ok'):
            users = api_call.get('members')
            for user in users:
                if 'name' in user:
                    if "real_name" in user:
                        user_name = user["real_name"]
                    else:
                        user_name = user["name"]
                    self._members[user.get('id')] = user_name.lower()
                    self._members[user_name.lower()] = user.get('id')

                    if user.get('name') == self._bot_name:
                        self._bot_id = user.get('id')

        # C85T359CM
        for group in groups_info["groups"]:
            self._channel_bot_is_member[group['id']] = group["members"]
            # self._slack_client.api_call("chat.postMessage",
            #                         channel=group['id'],
            #                         text="<!channel> Hey guys, i am here to remind you that the biweekly pub show is in a 6 days!!! :scream:\n Try to think about intresting things to talk about. If you need any \"person of intrest\" from other groups to attend, please invite them.\n\n On a personal note i plan to get better and to be here to suggest to you what to talk about in the future, and to help in any way i can :grinning:",
            #                         as_user=True
            #                         )

    def listen(self):
        if self._slack_client.rtm_connect(with_team_state=False):
            print "Successfully connected, listening for commands"
            while True:
                it = self._selector.select()
                it.handle()
        else:
            exit("Error, Connection Failed")

    def _register_event(self):
        event_registrar = self._selector.get_event_registrar()
        event_registrar.register(EventType.ACCEPT, HandlerAccept)
        event_registrar.register(EventType.SMALLTALK, HandlerSmalltalk)
        event_registrar.register(EventType.IFTTT, HandlerIFTTT)
        event_registrar.register(EventType.HELP, HandlerHelp)
        event_registrar.register(EventType.NOTIFY, HandlerNotify)
        event_registrar.register(EventType.REGISTER, HandlerRegister)
        event_registrar.register(EventType.OTHER, HandlerOther)
        event_registrar.add_event(EventAccept(self._bot_id, self._slack_client, self._channel_bot_is_member, self._im_bot_is_member))


if __name__ == "__main__":
    bot = SlackBot(SLACKBOT_CLIENT_ACCESS_TOKEN)
    bot.listen()


# https://stackoverflow.com/questions/41111227/how-can-a-slack-bot-detect-a-direct-message-vs-a-message-in-a-channel