def memoize(f):
    """python decorator or monad like structure to cache
        the values that the function generates.
    """
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function