"""
https://leetcode.com/problems/3sum/
判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组
"""

import unittest
from typing import List


def three_sum_equal_zero(nums: List[int]) -> List[List[int]]:
    result = []
    return result


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([2, 7, 11, 15], []),
        ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]])
    ]

    def test(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, three_sum_equal_zero(nums))
