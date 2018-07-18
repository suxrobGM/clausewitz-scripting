
class StateHistory(object):
    """Class of State History"""

    owner = ""
    stateFlags = []
    victoryPoints = {}
    effects = []
    buildings = { 'infrastructure':0,  
                      'arms_factory':0, 
                      'air_base':0, 
                      'industrial_complex':0, 
                      'naval_base':0, 
                      'bunker':0, 
                      'coastal_bunker':0, 
                      'dockyard':0, 
                      'anti_air_building':0,
                      'synthetic_refinery':0, 
                      'radar_station':0, 
                      'rocket_site':0, 
                      'nuclear_reactor':0,
                      'steel_factory':0, 
                      'aluminium_factory':0, 
                      'chromium_factory':0, 
                      'tungsten_factory':0
                      }
       
        