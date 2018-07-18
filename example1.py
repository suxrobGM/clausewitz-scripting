#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Подключить все модулы
from clausewitz_script import *

countries = ["RUS", "ENG", "USA", "GER"] #список государств

trigger_simple = [
    Trigger.has_idea("1"),
    Trigger.has_idea("2"),
    Trigger.has_idea("3"),
    [Trigger.has_idea("4"), Trigger.has_idea("5")]
    ]
If_simple = If(trigger_simple, Effect.add_stability(45))

#Объединяем несколько условии в одном переменный "trigger" 
trigger = AND(
            Trigger.has_idea("free_trade"),
            Trigger.is_in_faction(False),
            OR(
              [Trigger.TAG(tag) for tag in countries], #генерация несколько условии из списка countries
            )
           )


scope = Scope.TAG("ROOT",                                                             
                  If(trigger, Effect.add_stability(45))
                 )



#Показать результат программы на тестовом файле
f = open("test.txt", "w+")
for item in scope:
    f.write(item+"\n")

f.close()
print(trigger)
    


