"""
Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”
例如: 28 = 1 + 2 + 4 + 7 + 14

我的思路:
由于因数是正整数，除了1最小的因数是2，所以num的最大因数是num//2
另一种思路是穷举i32范围内的所有完美数，完美数一定是偶数，还可以用欧几里得-欧拉定理在O(1)的时间内辨别，不过没有穷举快
"""
import unittest
import math


def is_perfect_number(num: int) -> bool:
    """
    在枚举时，我们只需要从 1 到 sqrt(n) 进行枚举即可。
    这是因为如果 n 有一个大于 sqrt(n) 的因数 x，那么它一定有一个小于 sqrt(n) 的因数 n/x
    所以求一个较小因数的同时也记入较大因数即可，一对一对地数更快
    """
    # factors_sum = 1
    # for factor in range(num // 2, 1, -1):
    #     if num % factor == 0:
    #         factors_sum += factor
    # return factors_sum == num
    if num <= 1:
        return False
    if num == 6:
        return True
    factors_sum = 1
    for lower_factor in range(2, int(math.sqrt(num))):
        if num % lower_factor == 0:
            upper_factor = num // lower_factor
            factors_sum = factors_sum + lower_factor + upper_factor
    return factors_sum == num


perfect_numbers = {6, 28, 496, 8128, 33550336}


# perfect_numbers = {6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128}

# Rust的最佳解答(i32范围内所有完美数)
# return num == 6 || num == 28 || num == 496 || num == 8128 || num == 33550336
def is_perfect_number_2(num: int) -> bool:
    return num in perfect_numbers


class Testing(unittest.TestCase):
    TEST_CASES = [
        (28, True),
        # 会超时的测试用例
        (99999992, False)
    ]

    def test_is_perfect_number(self):
        for num, expected in self.TEST_CASES:
            self.assertEqual(expected, is_perfect_number(num))
