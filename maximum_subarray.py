"""
https://leetcode.com/problems/maximum-subarray/
"""
import unittest
from typing import List, Tuple


class Solution:
    @staticmethod
    def max_sub_array(nums: List[int]) -> int:
        size: int = len(nums)
        max_sum: int = 0
        for i in range(size):
            temp_sum = 0
            for j in range(i, size):
                temp_sum += nums[j]
                if temp_sum > max_sum:
                    max_sum = temp_sum
        return max_sum


class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[List[int], int]] = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    ]

    def test_solution(self):
        for input_array, expected in self.TEST_CASES[:]:
            self.assertEqual(expected, Solution.max_sub_array(input_array))
