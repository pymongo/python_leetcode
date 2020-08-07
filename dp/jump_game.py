"""
  2 3 1 1 4
2 T T T
3 T T T T T
1   T T T
1     T T T
4 T T T T T
"""
import unittest
from typing import List


class Solution:
    @staticmethod
    def can_jump_dp(nums: List[int]) -> bool:
        size = len(nums)
        # dp[i][j]表示从位置i能否跳到位置j
        dp = [[False] * size for _ in range(size)]
        # 初始条件 1. for j in range(nums[i]): dp[i][-j..j] == True
        for i in range(size):
            for j in range(max(i - nums[i], 0), min(i + nums[i]+1, size)):
                dp[i][j] = True
        # 状态转移方程: ???
        for i in range(1, nums[0]):
            pass
        # for row in dp:
        #     print(row)

        return False


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ]

    def test_can_jump_dp(self):
        for nums, can_jump in self.TEST_CASES:
            self.assertEqual(can_jump, Solution.can_jump_dp(nums))
