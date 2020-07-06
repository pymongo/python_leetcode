import unittest

# 如果反转后的整数i32溢出，则返回0
I32_MIN = -2 ** 31
I32_MAX = 2 ** 31 - 1


def reverse_number(n: int) -> int:
    is_negative: bool = False
    if n < 0:
        is_negative = True
        n = -n
    reverse: int = 0
    while n != 0:
        reverse = reverse * 10 + n % 10
        n //= 10
    if is_negative:
        return 0 if -reverse < I32_MIN else -reverse
    if not is_negative and reverse > I32_MAX:
        return 0
    return reverse


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        (123, 321),
        (-123, -321)
    ]

    def test(self):
        for num, expected in self.TEST_CASES:
            self.assertEqual(expected, reverse_number(num))
