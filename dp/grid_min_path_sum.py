import unittest
from typing import List


# 从左上到右下的最短路径，只能向右或向下走(Unique Path既视感)
# 和Unique Path的主要区别是, 求最值不是求方案总数，次要区别是本题的边都有「权重」
class Solution(unittest.TestCase):
    TEST_CASES = [
        ([
             [1, 3, 1],
             [1, 5, 1],
             [4, 2, 1]
         ], 7)
    ]

    def test_min_path(self):
        for grid, min_path in self.TEST_CASES:
            self.assertEqual(min_path, self.min_path(grid))

    @staticmethod
    def min_path(grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 用滚动数组/循环数组将空间复杂度优化到2行n列
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        # for row in dp:
        #     print(row)
        return dp[m-1][n-1]
