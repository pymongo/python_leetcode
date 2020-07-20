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
from copy import deepcopy


def solution(nums: List[int], target: int) -> int:
    nums.sort()
    size = len(nums)
    left, right = 0, size - 1
    count = 0
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        else:
            # 这步是关键，减少了O(n)的时间复杂度，既然数组是有序的，那么[left..right-1, right]的两两组合都是满足条件的
            count += right - left
            left += 1
    return count


# 与triangle-count用同一套模板
def second_two_sum_le(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    size = len(nums)
    left, right = 0, size - 1
    count = 0
    while left < right:
        print(left, right)
        print(nums[left], nums[right])
        if nums[left] + nums[right] <= target:
            # (left, left+1..right), (left,right), (left, right-1), ... , (left, left+1)
            # nums[left]=2, nums[right]=15: count += 3 => (2,15), (2,11), (2,7)
            # nums[left]=7, nums[right]=15: count += 2 => (7,15), (7,11)
            # nums[left]=11,nums[right]=15: count += 0 => right -= 1(break)
            # count会算上固定b之后[a..b-1, b]的所有解，然后b-=1; 而two_sum_le一题是固定a之后[a,a+1..b]所有解，所以a+=1
            count += right - left
            left += 1
        else:
            right -= 1
    return count


# https://www.lintcode.com/problem/two-sum-greater-than-target/description?_from=ladder&&fromId=161
def two_sum_gt(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    left, right = 0, len(nums) - 1
    count = 0
    while left < right:
        if nums[left] + nums[right] > target:
            count += right - left
            right -= 1
        else:
            left += 1
    return count


class Test(unittest.TestCase):
    TEST_CASES = [
        ([2, 7, 11, 15], 24, 5)
    ]

    def test(self):
        for nums, target, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, solution(nums, target))

    def test_second_two_sum_le(self):
        for nums, target, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, second_two_sum_le(nums, target))
