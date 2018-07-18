from .event import Event

class CountryEvent(Event):
    """Class of country event"""

    buffer = []   

    def __init__(self, fileName):
        self.fileName = fileName




