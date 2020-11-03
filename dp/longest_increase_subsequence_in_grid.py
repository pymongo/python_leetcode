import unittest
from typing import List


# lintcode only: 398. Longest Continuous Increasing Subsequence II
# 为什么棋盘行走类型的题也能用DP？因为棋盘行走按升序去走，数值会越走越大，不可能出现循环依赖
class Testing(unittest.TestCase):
    TESTCASES = [
        ([
             [1, 2],
             [5, 3]
         ], 4)
    ]

    def test(self):
        for grid, max_len in self.TESTCASES:
            self.assertEqual(max_len, self.f(grid))

    @staticmethod
    def f(grid: List[List[int]]) -> int:
        """
        思路: 排序+记忆化搜索
        这里演示非DFS的记忆化搜索
        用额外的数组排序后能减少很多运算量
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        points = []
        for i in range(m):
            for j in range(n):
                points.append((grid[i][j], i, j))
        points.sort()
        # key: (i,j), value: 接龙型终点是(i,j)的LIS(Longest Increase Subsequence)
        memo = dict()
        max_len = 1
        for point_idx in range(m * n):
            i, j = points[point_idx][1], points[point_idx][2]
            memo[(i, j)] = 1
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                last_i, last_j = i + di, j + dj
                if not (-1 < last_i < m and -1 < last_j < n):
                    continue
                # if grid[next_i][next_j] < points[point_idx][2]:
                #     continue
                # 接龙型DP: 换个思路，这里不找比point_idx更大的点，而是找「终点为point_idx」的点
                if (last_i, last_j) in memo and grid[last_i][last_j] < points[point_idx][0]:
                    memo[(i, j)] = max(memo[(i, j)], memo[(last_i, last_j)] + 1)
                    max_len = max(max_len, memo[(i, j)])
        return max_len
