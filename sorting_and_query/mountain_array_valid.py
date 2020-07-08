"""
https://leetcode.com/problems/find-in-mountain-array/
"""
import unittest
from typing import List


def valid(nums: List[int]) -> bool:
    return False


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([2, 1], False),
        ([3, 5, 5], False),
        ([0, 3, 2, 1], True),
    ]

    def test_valid(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, valid(nums))
