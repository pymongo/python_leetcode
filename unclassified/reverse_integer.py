import unittest

# 如果反转后的整数i32溢出，则返回0
I32_MIN = -2 ** 31
I32_MAX = 2 ** 31 - 1


def reverse(n: int) -> int:
    return -1


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        (123, 321),
        (-123, -321)
    ]

    def test(self):
        for num, expected in self.TEST_CASES:
            self.assertEqual(expected, reverse(num))
