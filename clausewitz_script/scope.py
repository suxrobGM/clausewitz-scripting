from .utils import _build_block_of_operators

class Scope(object):
    """
    English: Static class of game scopes
    Русский:
    """

    @staticmethod
    def TAG(countryTag = str(), *args):
        """
        English: 
        Русский: 
        """
        return _build_block_of_operators(countryTag, *args)
