from .statehistory import StateHistory
from .effect import Effect

class State(object):
    """Class of state"""
    
    buffer = []
    ID = 0
    stateName = ""
    manpower = 0
    state_category = ""
    resources = {"oil":0, "aluminium":0, "rubber":0, "tungsten":0, "steel":0, "chromium":0 }
    history = StateHistory() 
    provincies = []

    def __init__(self, fileName):
        self.fileName = fileName 
        
    def SetLocalisation(self, language, key, text):
        fileName = "state_names_pyg_l_"+language+".yml"
        locRaws = []
        locRaws.append("l_"+language+":")
        locRaws.append(key+':0 '+'\"'+text+'\"')

    def Build(self):
        """Создать регион исходя из всех данные объекта State"""
        self.buffer.append("state = {")
        self.buffer.append("\t"+"id = %d" %(self.ID))
        self.buffer.append("\t"+"name = %s" %(self.stateName))
        self.buffer.append("\t"+"manpower = %s" %(self.manpower))
        self.buffer.append("\t"+"state_category = %s" %(self.state_category))

        self.buffer.append("\t"+"resources = {")
        for key, value in self.resources.items():
            if value != 0:
                self.buffer.append("\t\t"+key+"="+str(value))
        self.buffer.append("\t"+"}") #end of resources
        
        self.buffer.append("\t"+"history = {")              
        self.buffer.append("\t\t"+"owner = "+self.history.owner)

        for flag in self.history.stateFlags:
            self.buffer.append("\t\t"+"set_state_flag = "+flag)
        
        #effects block
        for effect in self.history.effects:
            self.buffer.append("\t\t"+effect)

        #VP block
        self.buffer.append("\t\t"+"victory_points = {")
        for key, value in self.history.victoryPoints.items():
            if value != 0:
                self.buffer.append("\t\t\t"+str(key)+" "+str(value))
        self.buffer.append("\t\t"+"}") #end of vp block

        self.buffer.append("\t\t"+"buildings = {")
        for key, value in self.history.buildings.items():
            if value != 0:
                self.buffer.append("\t\t\t"+key+"="+str(value))         
        self.buffer.append("\t\t"+"}") #end of buildings     
        
        self.buffer.append("\t"+"}") #end of history
        
        provinciesString = ""    
        for item in self.provincies:
            provinciesString += " {}".format(str(item))         
            
        self.buffer.append("\t"+"provinces = {%s }" %(provinciesString))
        self.buffer.append("}") #end of state         

    
