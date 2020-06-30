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
    nums.sort()
    size = len(nums)
    left, right = 0, size-1
    count = 0
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        else:
            # 这步是关键，减少了O(n)的时间复杂度，既然数组是有序的，则从(left,right)到right的两两组合都是满足条件的
            count += right - left
            left += 1
    return count


class Test(unittest.TestCase):
    TEST_CASES = [
        ([2, 7, 11, 15], 24, 5)
    ]

    def test(self):
        for nums, target, expected in self.TEST_CASES[:]:
            self.assertEqual(expected, solution(nums, target))
