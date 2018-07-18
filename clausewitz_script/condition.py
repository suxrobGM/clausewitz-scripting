from .utils import _build_block_operator 

def OR(*args):
    """
    Логический OR
    Принимает только объекты Trigger
    Функция возвращает список условии
    """
    return _build_block_operator("OR", *args)


def AND(*args):
    """
    Логический AND
    Принимает только объекты Trigger
    Функция возвращает список условии
    """   
    return _build_block_operator("AND", *args)


def NOT(*args):
    """
    Логический NOT
    Принимает только объекты Trigger
    Функция возвращает список условии
    """ 
    return _build_block_operator("NOT", *args)
