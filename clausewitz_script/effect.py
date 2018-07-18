
class Effect(object):
    """Static class of game effects"""
     
    @staticmethod
    def Add_Core_Of(countryTag):
        """Регион станет считаться национальной территорией государства {countryTag}"""
        return "add_core_of = {}".format(countryTag)

    @staticmethod
    def Add_Stability(value = 0):
       """Прирост базовой стабильности: {int|value}"""
       return "add_stability = {}".format(value)


