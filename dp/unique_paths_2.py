import unittest
import collections
from typing import List


class Solution:
    @staticmethod
    def is_possible_to_reach_end(grid: List[List[int]], rows: int, cols: int) -> bool:
        if grid[0][0] == 1:
            return False
        end_point = (rows - 1, cols - 1)
        if end_point == 1:
            return False
        visited = set()
        queue = collections.deque()
        queue.append((0, 0))
        while queue:
            row, col = queue.popleft()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if (row, col) == end_point:
                return True
            for row_offset, col_offset in ((0, 1), (1, 0)):
                next_row, next_col = row + row_offset, col + col_offset
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue
                if grid[next_row][next_col] == 1:
                    continue
                queue.append((next_row, next_col))
        return False

    # noinspection PyMethodMayBeStatic,PyPep8Naming
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0] * cols for _ in range(rows)]
        # 原数组中，用负数-1表示有1个方案，以此区分障碍物1
        for row in range(rows):
            if grid[row][0] == 1:
                # 因为只能向右或向下走(不存在围着障碍物绕一圈的走法)，遇到障碍物，则往右都不可能到达
                break
            dp[row][0] = 1
        # 这题就不能像三角形那题一样，DP数组也是入参数组，因为初始化完第一行后，所有障碍物会变成0，再去初始化列时就丢失了障碍物的信息
        for col in range(cols):
            if grid[0][col] == 1:
                break
            dp[0][col] = 1

        for row in range(1, rows):
            for col in range(1, cols):
                if grid[row][col] == 1:
                    continue
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[rows - 1][cols - 1]


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([
             [0, 0, 0],
             [0, 1, 0],
             [0, 0, 0]
         ], 2),
        ([[1, 0], [0, 0]], 0),
        ([[1, 0]], 0),
        ([[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
          [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
          [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
          [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
          [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
          [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
          [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]], 13594824)
    ]

    def test_dp_solution(self):
        solution = Solution()
        for obstacle_grid, paths_count in self.TEST_CASES:
            print(len(obstacle_grid), paths_count)
            self.assertEqual(paths_count, solution.uniquePathsWithObstacles(obstacle_grid))
