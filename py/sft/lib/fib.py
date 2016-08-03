from util import memoize

@memoize
def fibonacci(n):
    """
        Dynamic programming approach for fibonacci method.
        It uses a decorator that keeps track of the calls
        using a cache dictionary and reduces the redundant
        calls.
    :param n:    integer number n
    :return:     nth fibonacci number
    """
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)
