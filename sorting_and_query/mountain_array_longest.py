"""
https://leetcode.com/problems/longest-mountain-in-array/solution/shu-zu-zhong-de-zui-chang-shan-mai-by-leetcode/
"""
import unittest
from typing import List


def longest_mountain_in_array(nums: List[int]) -> int:
    return -1


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([2, 1, 4, 7, 3, 2, 5], 5),
        ([2, 2, 2], 0),
    ]

    def testing(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, longest_mountain_in_array(nums))
