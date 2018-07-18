
class Trigger(object):
    """Static class of game triggers"""

    @staticmethod
    def IsInFaction(value = bool()):
        """
        English: Checks that country is in some faction
        Русский: Проверяет, что государства cостоит в альянсе
        """
        if value == True:
            return "is_in_faction = yes"
        else:
            return "is_in_faction = no"
        

    @staticmethod
    def TAG(countryTag = str()):
        """ """
        return "tag = {}".format(countryTag)

    @staticmethod
    def HasIdea(ideaName = str()):
        """
        English: Checks that country has an specific{ideaName} idea
        Русский: Проверяет, что страна имеет указанную{ideaName} идею
        """
        return "has_idea = {}".format(ideaName)


