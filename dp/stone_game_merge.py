import unittest
import sys
from typing import List


# 石子归并游戏
# 思考: 从终点到起点的动态规划，不管怎么划分，最后一次合并的耗时一定是sum(nums)
# 假设最后一次合并的左半区域是x，右边是y，动态规划就是在找这刀分隔线切在哪
# dp[i][j]表示下标i一直合并到j的最小耗费
class Solution(unittest.TestCase):
    TEST_CASES = [
        # 1和1先合并 => 4,2,4 => 6,4
        ([4, 1, 1, 4], 18),
        # 4和3、3和4先合并
        ([4, 3, 3, 4], 28),
    ]

    def test(self):
        for nums, min_cost in self.TEST_CASES:
            self.assertEqual(min_cost, self.f(nums))

    @staticmethod
    def f(nums: List[int]) -> int:
        """
        状态表示: dp[i][j]表示下标i一直合并到j的最小耗费
        初始化: dp[i][i] = 0
        答案: dp[0][n-1]
        状态转移:
        for k in range(i, j)
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+sum(nums[i:j+1]))
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [[0] * n for _ in range(n)]

        # 初始化前缀和数组，用于快速算出sum(nums[i:j])
        prefix_sum = nums.copy()
        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]
        # 确保i=-1时，前缀和prefix_sum[-1]=0，也就是不选任何数
        # 这样的好处是i=0,j=j时，sum(nums[i:j+1])=prefix_sum[j]-prefix_sum[0-1]
        prefix_sum.append(0)

        # 区间型动态规划的填表方法: ↘️方向斜着填
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                sum_i_j = prefix_sum[j] - prefix_sum[i - 1]
                # 在求最小的时候，需要初始化成一个很大的数，然后不断更新
                dp[i][j] = sys.maxsize
                for mid in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j] + sum_i_j)
        # for i in range(n):
        #     print(dp[i])
        return dp[0][n - 1]
