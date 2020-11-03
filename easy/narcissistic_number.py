"""
narcissistic(水仙花数): 一个n位数，每位的n次方之和等于本身
例如: 0-9是水仙花数，因为3**1=3
例如: 153 = 1^3 + 5^3 + 3^3
问题: 请范围n-n位数内有几个水仙花数，例如n=3时只返回100-999范围内的水仙花数
"""
import unittest
from typing import List


class Solution(unittest.TestCase):
    TESTCASES = [
        # 1位数里有10个水仙花数
        (1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        # 没有二位数的水仙花数
        (2, []),
        (6, [548834]),
    ]

    def test(self):
        for n, narcissistic_nums in self.TESTCASES:
            self.assertEqual(narcissistic_nums, self.get_narcissistic_numbers(n))

    @staticmethod
    def get_narcissistic_numbers(n: int) -> List[int]:
        """
        没有用到特殊的算法，直接暴力枚举就行了
        """
        if n == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if n == 2:
            return []

        res = []
        for num in range(10 ** (n - 1), 10 ** n):
            number = num
            digits_sum = 0
            while number != 0:
                digits_sum += (number % 10) ** n
                number //= 10
            if digits_sum == num:
                res.append(num)
        return res
