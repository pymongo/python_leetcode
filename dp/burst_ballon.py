import unittest
from typing import List


# 终点倒推的区间型动态规划: 一定存在一个气球🎈是最后被戳爆的
class Solution(unittest.TestCase):
    TEST_CASES = [
        # 可以想象数组左右两边各有一个隐藏的1，吹爆1得分3*1*5=15，吹爆3得分(1*)3*5，所以总分是15+15+5
        ([3, 1, 5], 35),
    ]

    def test(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, self.f(nums))

    # TODO functools.lru_cache
    # TODO 如果用记忆化搜索DFS做，要给DFS函数打上装饰器@lru_cache(None)
    # TODO @lru_cache(None)能禁用lru，牺牲空间换取时间上运行性能更快
    @staticmethod
    def f(nums: List[int]) -> int:
        # 左右两边补上1
        nums = [1, *nums, 1]
        n = len(nums)

        # dp[i][j]表示戳爆(i,j)之间所有气球的最大积分(不含i,j)
        dp = [[0] * n for _ in range(n)]

        # 长度小于2的区间都没有任何气球被戳爆，积分为0
        # 填表时大区间依赖于小区间(自上而下)
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                mul_ij = nums[i] * nums[j]
                for mid in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][mid] + dp[mid][j] + nums[mid] * mul_ij)
                    # dp[i][j] = max(dp[i][j], dp[i][mid] + dp[mid][j] + nums[i] * nums[mid] * nums[j])

        # 除了第一个气球1和最后1个气球以外，中间的所有气球
        return dp[0][n-1]
