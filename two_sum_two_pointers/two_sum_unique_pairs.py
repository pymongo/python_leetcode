"""
https://www.lintcode.com/problem/two-sum-unique-pairs/description?_from=ladder&&fromId=161
本题去重的部分有点像三数之和一题
"""

import unittest
from typing import List

# 面试问题: 是否可以先去重? -> 不可以
def solution(nums: List[int], target: int) -> int:
    # shadowing outer scope nums
    nums = sorted(nums)
    size = len(nums)
    last = size - 1
    left, right = 0, last
    count = 0
    while left < right:
        two_sum = nums[left] + nums[right]
        if two_sum == target:
            # 应对11+11=22情况
            # 去重部分一定要放在Equal分支内才能AC
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
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
