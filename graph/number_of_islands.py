import unittest
from typing import List


def my_dfs(grid: List[List[int]], rows: int, cols: int, i: int, j: int):
    if not (-1 < i < rows and -1 < j < cols):
        return
    if grid[i][j] == 0:
        return
    # DFS过程中将遍历过的岛屿设为0
    grid[i][j] = 0
    # 往上下左右扩散
    my_dfs(grid, rows, cols, i - 1, j)
    my_dfs(grid, rows, cols, i + 1, j)
    my_dfs(grid, rows, cols, i, j - 1)
    my_dfs(grid, rows, cols, i, j + 1)


def my_dfs_helper(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    islands_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                continue
            my_dfs(grid, rows, cols, i, j)
            islands_count += 1
    return islands_count


def my_bfs():
    pass


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([
             [1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [0, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1]
         ], 3)
    ]

    def test_my_dfs(self):
        for m, expected in self.TEST_CASES:
            self.assertEqual(expected, my_dfs_helper(m))
