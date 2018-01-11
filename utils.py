def get_in_message_bot_id(bot_id):
    return "<@" + bot_id + ">"


def clean_bot_id(bot_id):
    return bot_id.replace(">", "").replace("<", "").replace("@", "")
