import unittest
from typing import List


# 本题属于「接龙型」动态规划(也是坐标型动态规划的一种)
class Solution(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3], [[1, 2], [2, 3]]),
        ([1, 2, 4, 8], [[1, 2, 4, 8]]),
        ([3, 6, 9, 27, 81, 22, 24, 56, 243, 486, 726, 18, 36, 72], [[3, 9, 27, 81, 243, 486]])
    ]

    def test(self):
        for nums, subsets in self.TEST_CASES:
            self.assertIn(self.solution(nums), subsets)

    @staticmethod
    def solution(nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums = sorted(nums)
        size = len(nums)
        ptr = 1
        for i in range(1, size):
            if nums[i] % nums[i - 1] == 0:
                ptr += 1
            else:
                break
        return nums[:ptr]
