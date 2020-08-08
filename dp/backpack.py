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
    @staticmethod
    def backPack(m: int, A: List[int]) -> int:
        """
        @param m: An integer m denotes the size of a backpack
        @param A: Given n items with size A[i]
        @return: The maximum size
        """
        size = len(A)
        # 注意「前缀型」动态规划，i表示前i个物品选或不选，i的长度是len(nums)+1
        dp = [[False] * (m + 1) for _ in range(size + 1)]  # 注意range里面的是行，也就是i
        dp[0][0] = True
        # 开始填表
        for i in range(1, size + 1):
            dp[i][0] = True
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
            if dp[size][j]:
                return j
        return -1

    @staticmethod
    def min_partition(nums: List[int]) -> int:
        """
        本题要求将数组任意分成两部分，要求两部分之和 的差值最小
        实际上可以转化为01背包问题: 从数组中选任意个数，使得和尽可能接近sum(nums)//2
        不过这题的dp状态只能用dp[i][j]表示前i个数凑出<=j的最大和是多少，不能用布尔值
        如果用这种DP方程在lintcode上要特判`if size==209: return 1`和`if size>300: return 0`
        这题size * half_sum的数组太大了，有另一种优化DP数组空间复杂度的思路:
        TODO dpi表示两个集合之差为i的构造方法是否存在
        """
        full_sum = sum(nums)
        half_sum = full_sum // 2
        return abs(full_sum - 2 * Solution.dp_state_2(half_sum, nums))

    @staticmethod
    def dp_state_2(m: int, nums: List[int]) -> int:
        # dp[i][j]表示前i个数凑出<=j的最大和是多少
        size = len(nums)
        dp = [[0] * (m + 1) for _ in range(size + 1)]
        for i in range(1, size + 1):
            for j in range(1, m + 1):
                if j >= nums[i - 1]:
                    # 这种状态表示不如布尔值之间或运算快
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i - 1]] + nums[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[size][m]


class Testing(unittest.TestCase):
    TEST_CASES = [
        (10, [3, 4, 8, 5], 9),
        (12, [2, 3, 5, 7], 12),
    ]

    def test(self):
        for m, nums, max_size in self.TEST_CASES:
            self.assertEqual(max_size, Solution.backPack(m, nums))

    def test_min_partition(self):
        self.assertEqual(1, Solution.min_partition([1, 6, 11, 5]))
        self.assertEqual(0, Solution.min_partition([1, 2, 3, 4]))
