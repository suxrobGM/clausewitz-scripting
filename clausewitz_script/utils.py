
def _build_block_of_operators(operatorName = str(), *args):
    """
    Функция для посторение блочных операторов
    Например,
    RUS = {
        *args
    }
    Аргументы: 
        operatorName - имя оператора(OR, AND, NOT, *Tag* - тег страны и тп.)
        *args - список триггеров, эффектов, блочных операторов и тп.
    """
    buffer = []
    buffer.append("\t"+operatorName+" = {")   
    for arg in args:
        if isinstance(arg, list):
            #Проверка знак табуляции '\t'        
            for item in arg:                          
                #если нету ни каких табуляции тогда добавить сразу две '\t'               
                arg[arg.index(item)] = _check_tabs(item, 2)               
            buffer = buffer + arg
        else:          
            buffer.append(_check_tabs(arg, 2))
    buffer.append("\t"+"}")
    return buffer


def _build_block_of_condition_operators(operatorName = str(), conditions = list(), *args):
    """
    Функция для посторение блочных операторов с уловиями
    Напирмер, 
    if = { 
        limit { *conditions } 
        *args 
    }
    Аргументы: 
        operatorName - имя оператора(if, random_country, every_country и тп.)
        conditions - список триггеров
        *args - список эффектов, блочных операторов и тп.
    """
    buffer = []
    buffer.append("\t"+operatorName+" = {")

    # block of condition
    buffer.append("\t\t"+"limit = {")
    for condition in conditions:
        if isinstance(condition, list):
            #Проверка знак табуляции '\t' если объект является список       
            for item in condition:                          
                condition[ condition.index(item) ] = _check_tabs(item, 3)
            buffer = buffer + condition
        else: #Проверка знак табуляции '\t' если объект является строка        
            buffer.append(_check_tabs(condition, 3))            
                
    buffer.append("\t\t"+"}") # end of condition block
    
    # block of effects
    for arg in args:
        if isinstance(arg, list):
            #Проверка знак табуляции '\t'        
            for item in arg:                          
                #если нету ни каких табуляции тогда добавить сразу две '\t'               
                arg[arg.index(item)] = _check_tabs(item, 2)               
            buffer = buffer + arg
        else:          
            buffer.append(_check_tabs(arg, 2))
    buffer.append("\t"+"}") # end of operator block
    return buffer


def _check_tabs(string = str(), minimum_tabs = 1):
    """
    Проверка количества знак табуляции в начале строки
    string - проверямый строка
    minimum_tabs - количества символ табуляции как минимум должна быть в начале строки
    return: строка с необходимое символ табуляции 
    """
    count = 0
    for char in string:
        if char == '\t':
            count += 1
        if char.isalpha():
            break
    if count < minimum_tabs:        
        string = (minimum_tabs - count)*'\t' + string      
    else:
        string ='\t' + string
    return string
