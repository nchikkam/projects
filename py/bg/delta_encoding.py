import unittest

"""
    [25626, 25757, 24367, 24267, 16, 100, 2, 7277]
    delta = a[i]-a[i-1] for all i >=1
    if -127 <= delta <= 127 then just output delta other wise attach -128
     for that delta.
"""
def deltaEncode(seq):
    ret = []
    l = len(seq)
    ret.append(seq[0])

    for i in range(1, l):
        delta = seq[i]-seq[i-1]
        if delta < -127 or delta > 127:
            ret.append(-128)
            ret.append(delta)
        else:
            ret.append(delta)
    return ret

class DeltaEncodeTest(unittest.TestCase):
    def test_sample(self):
        seq = [25626, 25757, 24367, 24267, 16, 100, 2, 7277]
        actual = deltaEncode(seq)
        expected = [25626, -128, 131, -128, -1390, -100, -128, -24251, 84, -98, -128, 7275]
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()