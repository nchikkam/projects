import unittest

def match_pwd_criteria(pwd):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    upper_chars = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z']
    uppers_char_flag = False

    for digit in digits:
        if digit in pwd:
            return False

    for char in upper_chars:
        if char in pwd:
            uppers_char_flag = True
            break

    return uppers_char_flag

def solution(S):
    l = len(S)
    sol = -1

    for i in range(l+1):
        for j in range(i, l+1):
            pwd = []
            for k in range(i, j):
                pwd.append(S[k])

            if match_pwd_criteria(pwd):
                if len(pwd) > sol:
                    sol = len(pwd)

    return sol

class PasswordVerifier(unittest.TestCase):

    def test_cases(self):
        self.assertEqual(solution("a0Ba"), 2)
        self.assertEqual(solution("Ba"), 2)
        self.assertEqual(solution("Ba0"), 2)

        self.assertEqual(solution("a"), -1)
        self.assertEqual(solution("0"), -1)
        self.assertEqual(solution(""), -1)
        self.assertEqual(solution("a0BAc0C0Da"), 3)

if __name__ == "__main__":
    unittest.main()