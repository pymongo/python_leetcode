"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/
给n个整数的山脉数组，即先增后减的序列，找到山顶(最大值)
"""

import unittest
from typing import List


def peak_index_brute_force(nums: List[int]) -> int:
    i = 0
    while nums[i] < nums[i+1]:
        i += 1
    return i


def peak_index(nums: List[int]) -> int:
    return -1


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([0, 1, 0], 1),
        ([0, 2, 1, 0], 1),
    ]

    def test_peak_index_brute(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, peak_index_brute_force(nums))

    def test_peak_index(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, peak_index(nums))
