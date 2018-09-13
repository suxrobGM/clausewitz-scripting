#!/usr/bin/env python
# -*- coding: utf-8 -*-

from clausewitz_script import State, Effect
from os import DirEntry

if __name__ == '__main__':    
    
    newState = State(fileName="750-New State.txt")

    newState.ID = 750
    newState.stateName = "New_State"
    newState.manpower = 45646
    newState.state_category = "town"
    newState.resources = { "oil":5, "steel":10, "rubber":6 }
    newState.history.owner = "RUS"
    newState.history.stateFlags = [ "christianity" ]
    newState.history.victoryPoints = { 9620: 30 }
    newState.history.buildings = { "arms_factory": 6, "infrastructure": 4 }   
    newState.history.effects = [ Effect.add_core_of("RUS") ]
    newState.provincies = [ 13365, 13366, 13644 ]
    newState.SetLocalisation(language="russian", key="New_State", text="Новый регион")
    newState.Build()
       

    for item in newState.buffer:
        print(item)
    
    
