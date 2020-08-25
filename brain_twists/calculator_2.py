import unittest


class Solution(unittest.TestCase):
    TEST_CASES = [
        ("1 + 1", 2),
    ]

    def test(self):
        for s, res in self.TEST_CASES:
            self.assertEqual(res, self.calculate(s))

    @staticmethod
    def calculate(s: str) -> int:
        stack = []
        rhs, sign = 0, '+'

        n = len(s)
        for i in range(n):
            if s[i].isdigit():
                rhs = rhs * 10 + int(s[i])
            if s[i] in '+-*/' or i == n - 1:
                if sign == '+':
                    stack.append(rhs)
                elif sign == '-':
                    stack.append(-rhs)
                elif sign == '*':
                    stack[-1] *= rhs
                elif sign == '/':
                    stack[-1] = int(stack[-1] / rhs)
                rhs, sign = 0, s[i]
        return sum(stack)
