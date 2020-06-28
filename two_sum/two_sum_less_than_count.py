"""
https://www.lintcode.com/problem/two-sum-less-than-or-equal-to-target/
Input: nums = [2, 7, 11, 15], target = 24.
Output: 5.
Explanation:
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 24
"""

import unittest
from typing import List


def solution(nums: List[int], target: int) -> int:
    return -1


class Test(unittest.TestCase):
    TEST_CASES = [
        ([2, 7, 11, 15], 24, 5)
    ]

    def test(self):
        for nums, target, expected in self.TEST_CASES[:]:
            self.assertEqual(expected, solution(nums, target))
