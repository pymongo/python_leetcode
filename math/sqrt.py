"""
https://lintcode.com/problem/sqrtx-ii/description?_from=ladder&&fromId=161
https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
number=16
init: guess=16/2=8
guess=(8+16/8)/2=5
guess=(5+16/5)/2=4.001...
// ...
难点在于退出循环的条件
我认为是当前的guess与新的guess相差小于千分之一时就可以break了
"""

import unittest
import random
import math


class Solution(unittest.TestCase):

    def test_my_sqrt(self):
        # print(my_sqrt(25))
        for _ in range(100):
            num = random.randint(1, 1000)
            self.assertLessEqual(abs(int(math.sqrt(num)) - self.sqrt_newton_iterative(num)), 1e-3)

    # 用牛顿连续均值迭代法会比二分法快得多，迭代次数少很多
    @staticmethod
    def sqrt_newton_iterative(num: int) -> int:
        if num == 0:
            return 0
        # 牛顿法的初始值是num/2
        last_n, n = num, num / 2
        # 由于牛顿迭代法，next_n一定会比当前的n小，所以不需要加abs
        while last_n - n > 1e-3:
            last_n = n
            n = (last_n + num / last_n) / 2
        return int(n)

    def test_is_perfect_square(self):
        self.assertTrue(self.is_perfect_square(16))
        self.assertFalse(self.is_perfect_square(14))

    @staticmethod
    def is_perfect_square(num: int) -> bool:
        # 牛顿法的初始值是num/2
        last_n, n = num, num / 2
        while last_n - n > 1e-4:
            last_n = n
            n = (last_n + num / last_n) / 2
        return int(n) ** 2 == num
