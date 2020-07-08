"""
https://leetcode.com/problems/find-in-mountain-array/
"""
import unittest
from typing import List


def valid(nums: List[int]) -> bool:
    length = len(nums)
    if length < 3:
        return False
    # 是否单调递增
    last_item_is_increasing = nums[0] < nums[1]
    if not last_item_is_increasing:
        return False
    for i in range(2, length):
        if nums[i-1] > nums[i]:
            last_item_is_increasing = False
        elif nums[i-1] < nums[i]:
            # 山脉数组不允许先递减(False)后递增(True)
            if not last_item_is_increasing:
                return False
            last_item_is_increasing = True
        else:
            return False
    if not last_item_is_increasing:
        return True
    else:
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
