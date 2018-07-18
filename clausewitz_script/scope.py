from .utils import _build_block_operator

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
        return _build_block_operator(countryTag, *args)
