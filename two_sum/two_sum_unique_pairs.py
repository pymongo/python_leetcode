"""
https://www.lintcode.com/problem/two-sum-unique-pairs/description?_from=ladder&&fromId=161
本题去重的部分有点像三数之和一题
"""

import unittest
from typing import List


def solution(nums: List[int], target: int) -> int:
    # shadowing outer scope nums
    nums = sorted(nums)
    size = len(nums)
    last = size - 1
    left, right = 0, last
    # 应对11+11=22情况
    is_count_two_equals = False
    count = 0
    while left < right:
        # 不用set去重，因为太慢了
        while left < right and nums[left] == nums[left + 1]:
            # if not is_count_two_equals and nums[left] * 2 == target:
            #     count += 1
            #     is_count_two_equals = True
            left += 1
        while left < right and nums[right] == nums[right - 1]:
            # if not is_count_two_equals and nums[right] * 2 == target:
            #     count += 1
            #     is_count_two_equals = True
            right -= 1
        two_sum = nums[left] + nums[right]
        if two_sum == target:
            count += 1
            left += 1
            right -= 1
        elif two_sum > target:
            right -= 1
        else:
            left += 1
    return count


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([7, 11, 11, 1, 2, 3, 4], 22, 1),
        ([1, 1, 2, 45, 46, 46], 47, 2),
        ([1, 1], 2, 1)
    ]

    def test(self):
        for nums, target, count in self.TEST_CASES:
            self.assertEqual(count, solution(nums, target))
