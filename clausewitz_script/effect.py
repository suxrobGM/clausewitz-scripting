
class Effect(object):
    """Static class of game effects"""
     
    @staticmethod
    def add_core_of(countryTag):
        """Регион станет считаться национальной территорией государства {countryTag}"""
        return "add_core_of = {}".format(countryTag)

    @staticmethod
    def add_stability(value = 0):
       """Прирост базовой стабильности: {int|value}"""
       return "add_stability = {}".format(value)


