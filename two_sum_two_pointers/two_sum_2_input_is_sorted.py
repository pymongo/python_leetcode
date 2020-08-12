"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

import unittest
from typing import List


def two_sum_2(nums: List[int], target: int) -> List[int]:
    start, end = 0, len(nums) - 1
    while start < end:
        two_sum = nums[start] + nums[end]
        if two_sum > target:
            end -= 1
        elif two_sum < target:
            start += 1
        else:
            return [start+1, end+1]


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([2, 7, 11, 15], 9, [1, 2])
    ]

    def test(self):
        for nums, target, expected in self.TEST_CASES:
            self.assertEqual(expected, two_sum_2(nums, target))
