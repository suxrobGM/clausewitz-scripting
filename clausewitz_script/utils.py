
def _build_block_operator(operatorName = str(), *args):
    buffer = []
    buffer.append("\t"+operatorName+" = {")   
    for arg in args:
        if isinstance(arg, list):
            #Проверка знак табуляции '\t'        
            for item in arg:                          
                if item.find("\t") == -1: #если нету ни каких табуляции тогда добавить сразу две '\t'
                    temp = "\t\t" + item
                    arg[arg.index(item)] = temp
                else: #увеличить число табуляции
                    temp = "\t" + item
                    arg[arg.index(item)] = temp
            buffer = buffer + arg
        else:
            buffer.append("\t\t"+str(arg))
    buffer.append("\t"+"}")
    return buffer
