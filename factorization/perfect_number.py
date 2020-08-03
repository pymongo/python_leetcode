"""
Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”
例如: 28 = 1 + 2 + 4 + 7 + 14

我的思路:
由于因数是正整数，除了1最小的因数是2，所以num的最大因数是num//2
另一种思路是穷举i32范围内的所有完美数
"""
import unittest


def is_perfect_number(num: int) -> bool:
    factors_sum = 1
    # [14..=2]
    for factor in range(num // 2, 1, -1):
        if num % factor == 0:
            factors_sum += factor
    return factors_sum == num


class Testing(unittest.TestCase):
    TEST_CASES = [
        (28, True)
    ]

    def test_is_perfect_number(self):
        for num, expected in self.TEST_CASES:
            self.assertEqual(expected, is_perfect_number(num))
