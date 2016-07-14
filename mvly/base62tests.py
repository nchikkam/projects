import unittest
from lib.base62 import (
    Base62Util
)

class Base62UtilTest(unittest.TestCase):

    def testBase62ToDecmialBasic(self):
        subject = Base62Util()
        self.assertEqual('O', subject.toBase(50))

    def testBase62ToDecmialSimpleCase(self):
        subject = Base62Util()
        self.assertEqual('12', subject.toBase(64))

    def testDecmialToBase62Basic(self):
        subject = Base62Util()
        self.assertEqual('50', subject.toDec('O'))

    def testDecmialToBase62SimpleCase(self):
        subject = Base62Util()
        self.assertEqual('64', subject.toDec('12'))

    def testSample(self):
        subject = Base62Util()
        self.assertEqual('sXDVELneo', subject.toBase(6323566249246720))
        self.assertEqual('mw0iXTwjK', subject.toBase(4916191365693440))

    def testRegression(self):
        subject = Base62Util()
        for i in range(5000):
            self.assertEqual(subject.toDec(subject.toBase(i)), str(i))

if __name__ == "__main__":
    unittest.main()