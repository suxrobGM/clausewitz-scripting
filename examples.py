#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Подключить модулы для работы с условном опрератором: AND, OR, NOT и триггером
from clausewitz_script import Trigger, OR, AND, NOT 

countries = ["RUS", "ENG", "USA", "GER"] #список государств

#Объединяем несколько условии в одном переменный "trigger" 
trigger = OR(
            Trigger.HasIdea("free_trade"),
            Trigger.IsInFaction(False),
            OR(
              [Trigger.TAG(tag) for tag in countries], #генерация несколько условии из списка countries
            )
           )


#Показать результат программы на консоле
for item in trigger:
    print(item)


