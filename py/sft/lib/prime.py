import math

def is_prime(n):
    """
        function to verify if a given number is prime
    :param n:  number n
    :return:   boolean value true if n is prime, false otherwise
    """
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1  # square  limit to shorten the checks

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True