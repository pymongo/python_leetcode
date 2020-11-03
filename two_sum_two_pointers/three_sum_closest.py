import unittest
import sys
from typing import List


def solution(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    size = len(nums)
    min_diff = sys.maxsize
    closest_sum = 0
    for i in range(size - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 固定第三个数，然后简化为two_sum = target-第三个数的问题
        left, right = i + 1, size - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if three_sum > target:
                right -= 1
            elif three_sum < target:
                left += 1
            else:
                return three_sum
            new_diff = abs(three_sum - target)
            if new_diff < min_diff:
                min_diff = new_diff
                closest_sum = three_sum
    return closest_sum


class Testing(unittest.TestCase):
    TESTCASES = [
        ([-1, 2, 1, -4], 2, 2),
        ([2, 7, 11, 15], 3, 20),
    ]

    def test(self):
        for nums, target, expected in self.TESTCASES:
            self.assertEqual(expected, solution(nums, target))
