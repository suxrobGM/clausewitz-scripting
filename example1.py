#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Подключить модулы для работы с условном опрератором: AND, OR, NOT и триггером
from clausewitz_script import Trigger, Scope, Effect, OR, AND, NOT

countries = ["RUS", "ENG", "USA", "GER"] #список государств

#Объединяем несколько условии в одном переменный "trigger" 
trigger = AND(
            Trigger.has_idea("free_trade"),
            Trigger.is_in_faction(False),
            OR(
              [Trigger.TAG(tag) for tag in countries], #генерация несколько условии из списка countries
            )
           )

scope = Scope.TAG("RUS", 
                  Effect.add_stability(45), 
                  Effect.add_core_of("USA"),
                  Scope.TAG("USA",
                            Effect.add_core_of(74))
                  )

#Показать результат программы на консоле
for item in scope:
    print(item)


