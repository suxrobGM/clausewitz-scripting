from .utils import _build_block_of_operators
from .utils import _build_block_of_condition_operators

def OR(*args):
    """
    English:
         
    Русский:
        Логический OR
        Принимает только объекты Trigger
        Функция возвращает список условии
    """
    return _build_block_of_operators("OR", *args)


def AND(*args):
    """
    English:
         
    Русский:
        Логический AND
        Принимает только объекты Trigger
        Функция возвращает список условии
    """   
    return _build_block_of_operators("AND", *args)


def NOT(*args):
    """
    English:
         
    Русский:
        Логический NOT
        Принимает только объекты Trigger
        Функция возвращает список условии
    """ 
    return _build_block_of_operators("NOT", *args)

def If(conditions = list(), *args):
    """
    English:
         
    Русский:
        
    """
    return _build_block_of_condition_operators("if", conditions, *args)