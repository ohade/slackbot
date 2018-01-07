from enum import Enum


class EventType(Enum):
    ACCEPT = 1
    SMALLTALK = 2
    HELP = 3
    IFTTT = 4
    NOTIFY = 5
    REGISTER = 6

    OTHER = 100

