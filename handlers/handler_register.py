from utils import clean_bot_id, get_in_message_bot_id
from pathlib import Path


class HandlerRegister:
    def __init__(self, event_info, event_registrar, members):
        self._event_info = event_info
        self._event_registrar = event_registrar
        self._members = members

    def handle(self):
        bot_id = self._event_info.get_bot_id()
        response = self._event_info.get_response()
        person_initiating_request = self._event_info.get_person_initiating_request()
        person_initiating_request = "<@" + person_initiating_request + ">"
        person_to_register = response.params["person_to_register"].lower()
        target = get_in_message_bot_id(clean_bot_id(response.params["target"]))
        print "####", target, bot_id

        print "IS person_to_register IN MEMBERS?!?!", "YES" if person_to_register in self._members else "NO"
        if self._members.get(person_to_register) is not None:
            person_to_register = get_in_message_bot_id(clean_bot_id(self._members.get(person_to_register)))

        text = "User: " + person_initiating_request + \
               ", request to Register: " + person_to_register + \
               ", to: " + target

        names = set()

        f = Path("{}.txt".format(bot_id))
        if f.is_file():
            with open("{}.txt".format(bot_id), "rb") as f:
                for line in f.readlines():
                    print "|"+line.strip()+"|"
                    names.add(line.strip())

        is_already_registered = person_to_register in names
        names.add(person_to_register)

        with open("{}.txt".format(bot_id), "wb") as f:
            for n in names:
                f.write(n + "\n")

        # notify the one that request to person_to_register the person
        if is_already_registered:
            # self._event_info.get_socket().api_call("chat.postMessage",
            #                                        channel=self._event_info.get_channel(),
            #                                        text="{} already registered to  bot: {}".format(person_to_register,
            #                                                                                        get_in_message_bot_id(
            #                                                                                            target)),
            #                                        as_user=True
            #                                        )
            self._event_info.get_socket().api_call("chat.postMessage",
                                                   channel=self._event_info.get_channel(),
                                                   text=text,
                                                   as_user=True
                                                   )
        else:
            # self._event_info.get_socket().api_call("chat.postMessage",
            #                                        channel=self._event_info.get_channel(),
            #                                        text="Registered {} to get info from bot: {}".format(person_to_register,
            #                                                                                             get_in_message_bot_id(
            #                                                                                                 target)),
            #                                        as_user=True
            #                                        )

            self._event_info.get_socket().api_call("chat.postMessage",
                                                   channel=self._event_info.get_channel(),
                                                   text=text,
                                                   as_user=True
                                                   )
        # self._event_registrar.()

        # if the register and the registry are not the same person then notify also the one that was registered
        # notify the one that was registered
        # if register_name != applicant_name:
        #     self._event_info.get_socket().api_call("chat.postMessage",
        #                                            channel=self._event_info.get_channel(),
        #                                            text="Registered by {} to get info from bot: {}".format(
        #                                                register_name, bot_id),
        #                                            as_user=True
        #                                            )
