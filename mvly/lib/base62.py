from math import floor

"""
    In base62 number system the base is 62.
    The system consists of 62 different symbols just like
    hex contains 16 symbols [0-9, A-F]

    Symbols in Base 62:
    [a-z, A-Z, 0-9]
    26 + 26 + 10 = 62 different characters
"""
class Base62Util:

    def __init__(self):
        self.symbols = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.base = len(self.symbols)

    def toBase(self, num):
        """
            This method converts the given decimal number into base 62 radix.
        :param string: a number
        :return:       its base 62 representation
        """
        rem = num % self.base
        res = self.symbols[rem]
        quo = floor(num / self.base)
        while quo:
            r = quo % self.base
            quo = floor(quo / self.base)
            res = self.symbols[int(r)] + res
        return res

    def toDec(self, num):
        """
            This method converts given base62 number to decimal radix system.
        :param num: a bas62 number
        :return: the decimal form of given number
        """
        res = 0
        for i in range(len(num)):
            res = self.base * res + self.symbols.find(num[i])
        return str(res)