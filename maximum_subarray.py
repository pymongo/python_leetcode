"""
https://leetcode.com/problems/maximum-subarray/
"""
import unittest
from typing import List, Tuple


class Solution:
    @staticmethod
    def max_sub_array(nums: List[int]) -> int:
        size: int = len(nums)
        max_sum: int = nums[0]
        for i in range(size):
            temp_sum = nums[i]
            for j in range(i+1, size):
                temp_sum += nums[j]
                if max(temp_sum, nums[j]) > max_sum:
                    max_sum = max(temp_sum, nums[j])
        return max_sum


class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[List[int], int]] = [
        ([-1, 0, -2], 0),
        ([-2, 1], 1),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
    ]

    def test_solution(self):
        for input_array, expected in self.TEST_CASES[:]:
            print(input_array, expected)
            self.assertEqual(expected, Solution.max_sub_array(input_array))
