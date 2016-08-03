from prime import is_prime

def fizzbuzz(n):
    """
        "Buzz" when F(n) is divisible by 3.
        "Fizz" when F(n) is divisible by 5.
        "FizzBuzz" when F(n) is divisible by 15.
        "BuzzFizz" when F(n) is prime.
        the value F(n) otherwise.
    :param n:  integer
    :return:   a string that satisfies above criteria
    """
    if n % 3 == 0 and n % 5 == 0:
        ret = 'FizzBuzz'
    elif n % 3 == 0:
        ret = 'Buzz'
    elif n % 5 == 0:
        ret = 'Fizz'
    elif is_prime(n):
        ret = "BuzzFizz"
    else:
        ret = str(n)
    return ret