import unittest
import itertools


def check_reordered_power_of_2(n: int) -> bool:
    if n == 0:
        return False
    if (n & -n) == n:
        return True
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    size = len(digits)
    for nums in itertools.permutations(digits):
        if nums[0] == 0:
            continue
        num = sum(digit * (10 ** (size-1-i)) for i, digit in enumerate(nums))
        if (num & -num) == num:
            return True
    return False


class Testing(unittest.TestCase):
    TEST_CASE = [
        (1, True),
        (10, False),
        (16, True),
        (24, False),
        (46, True),
        # 214806876
    ]

    def test(self):
        for n, expected in self.TEST_CASE:
            print(n)
            self.assertEqual(expected, check_reordered_power_of_2(n))
