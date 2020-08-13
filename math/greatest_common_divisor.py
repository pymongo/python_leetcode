import unittest


# 辗转相除法求最大公约数(greatest_common_divisor)
class Solution(unittest.TestCase):
    TEST_CASES = [
        (10, 15, 5),
    ]

    def test(self):
        for a, b, gcd in self.TEST_CASES:
            self.assertEqual(gcd, self.gcd(a, b))

    @staticmethod
    def gcd(a: int, b: int) -> int:
        while a % b != 0:
            a, b = b, a % b
        return b
