from .event import Event

class NewsEvent(Event):
    """Class of news event"""

    buffer = []   

    def __init__(self, fileName):
        self.fileName = fileName




