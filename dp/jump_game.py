"""
  2 3 1 1 4
2 T T T
3   T T T T
1   T T T
1     T T T
4 T T T T T
TODO 隐含条件: 只能往右跳
"""
import unittest
from typing import List


class Solution:
    @staticmethod
    def can_jump_dp(nums: List[int]) -> bool:
        # Python的DP解法在leetcode上会超时
        size = len(nums)
        # dp[i]表示从位置i能否跳到终点
        dp = [False] * size
        first_max_jump = nums[0]
        for i in range(min(first_max_jump + 1, size)):
            dp[i] = True
        # 开始往右填表
        for i in range(first_max_jump + 1, size):
            # 遍历(除了0)从1到i-1(除了0以外，i左边的所有位置)的每个位置，判断是否存在一个位置能跳到位置i
            for j in range(1, i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    # break inner loop
                    break
        return dp[size - 1]

    @staticmethod
    def can_jump_greedy(nums: List[int]) -> bool:
        """
        依次遍历数组中的每一个位置，并实时维护 最远可以到达的位置
        """
        size, right_most = len(nums), 0
        last_index = size - 1
        for i in range(size):
            # 当前遍历的位置不能超过right_most，否则当前位置是无法跳到的
            if i <= right_most:
                right_most = max(right_most, i + nums[i])
                if right_most >= last_index:
                    return True
        return False


class Testing(unittest.TestCase):
    TESTCASES = [
        ([1, 1, 1, 0], True),
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ]

    def test_can_jump_dp(self):
        for nums, can_jump in self.TESTCASES:
            self.assertEqual(can_jump, Solution.can_jump_dp(nums))

    def test_can_jump_greedy(self):
        for nums, can_jump in self.TESTCASES:
            self.assertEqual(can_jump, Solution.can_jump_greedy(nums))
