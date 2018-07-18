from abc import ABC

class Event(ABC):
    """Abstract class of Event"""

    namespaces = []
    ID = ""
    title = ""
    desc = ""
    picture = ""
    isFireOnlyOnceEvent = False
    hidden = False
    isTriggeredOnly = False
    triggers = []
    options = []


