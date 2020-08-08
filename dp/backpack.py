"""
01型号背包问题，每个物品只能有选或不选两种状态
在n个物品中挑选若干物品装入容量为m的背包，最多能装多满
dp[i][j]表示从前i个物品中能否装成容量为j的组合
这题的状态转移方程有点像jump game
也可以用状态压缩性DP，每个物品的选或不选刚好是一个二进制，不过时间复杂度n*2^n
"""
import unittest
from typing import List


class Solution:

    # noinspection PyMethodMayBeStatic,PyPep8Naming
    def backPack(self, m: int, A: List[int]):
        """
        @param m: An integer m denotes the size of a backpack
        @param A: Given n items with size A[i]
        @return: The maximum size
        """
        size = len(A)
        # 注意前缀型动态规划，i表示前i个物品选或不选，i的长度是len(nums)+1
        dp = [[False] * (m + 1) for _ in range(size + 1)]  # 注意range里面的是行，也就是i
        dp[0][0] = True
        # 开始填表
        for i in range(1, size + 1):
            for j in range(1, m + 1):
                # A[i-1]是第i个数的下标
                if j >= A[i - 1]:
                    # 要么前i个数凑出了j的和(第i个数不选的情况) or 前i个数里凑出了j-第i个数的大小的和(第i个数选上的情况)
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
                else:
                    # dp[i - 1][j - A[i - 1]]中j-A[i-1]小于0越界
                    # 既第i个数的物品太大了，放进去超过背包容量j，所以没有将第i个数选上的分支
                    dp[i][j] = dp[i - 1][j]
        for j in range(m, -1, -1):
            print(j)
            if dp[size][j]:
                return j
        return -1



class Testing(unittest.TestCase):
    TEST_CASES = [
        (10, [3, 4, 8, 5], 9),
        (12, [2, 3, 5, 7], 12),
    ]

    def test(self):
        solution = Solution()
        for m, nums, max_size in self.TEST_CASES:
            self.assertEqual(max_size, solution.backPack(m, nums))
