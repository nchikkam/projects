def singleton(cls):
    """
        A decorator to keep single instance of the class. uses
        a dictionary to store the instance created and creates
        initially one.
    :param cls:   class
    :return:      the one and only single instance of the class.
    """
    _instances = {}

    def getinstance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return getinstance