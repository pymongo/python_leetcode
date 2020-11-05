"""
https://lintcode.com/problem/two-sum-closest-to-target/description?_from=ladder&&fromId=161
类似Two Sum，附加条件是如果没找到等于target的，则找最接近的。返回最接近的数与target之间的差分
"""
import sys
import unittest
from typing import List


# beats 93.60% Submissions
def my_solution(nums: List[int], target: int) -> int:
    min_diff = sys.maxsize
    nums = sorted(nums)
    left, right = 0, len(nums) - 1
    while left < right:
        two_sum = nums[left] + nums[right]
        new_diff = abs(two_sum - target)
        min_diff = min(min_diff, new_diff)
        if two_sum > target:
            right -= 1
        elif two_sum < target:
            left += 1
        else:
            return 0
    return min_diff


class Testing(unittest.TestCase):
    TESTCASES = [
        ([-1, 2, 1, -4], 4, 1),
        ([-1, -1, -1, -4], 4, 6),
    ]

    def test(self):
        for nums, target, diff in self.TESTCASES:
            self.assertEqual(diff, my_solution(nums, target))
