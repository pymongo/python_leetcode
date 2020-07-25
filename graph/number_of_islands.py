import unittest
import collections
from typing import List


def my_dfs(grid: List[List[int]], rows: int, cols: int, i: int, j: int):
    if not (-1 < i < rows and -1 < j < cols):
        return
    if grid[i][j] == 0:
        return
    # DFS过程中将遍历过的岛屿设为0(visited)
    grid[i][j] = 0
    # 往上下左右扩散
    my_dfs(grid, rows, cols, i - 1, j)
    my_dfs(grid, rows, cols, i + 1, j)
    my_dfs(grid, rows, cols, i, j - 1)
    my_dfs(grid, rows, cols, i, j + 1)


def my_dfs_helper(grid: List[List[int]]) -> int:
    if not grid:
        return 0
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


# BFS不容易解决的问题: 求最长路径
# DP不能解决的问题: 不能分层的图(分层的意思是图有方向性，不能绕圈)
def my_bfs(grid: List[List[int]]) -> int:
    if not grid:
        return 0
    islands_count = 0
    rows = len(grid)
    cols = len(grid[0])
    q = collections.deque()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                continue
            q.append((i, j))
            while q:
                row, col = q.popleft()
                if not (-1 < row < rows and -1 < col < cols):
                    continue
                if grid[row][col] == 0:
                    continue
                grid[row][col] = 0
                q.append((row - 1, col))
                q.append((row + 1, col))
                q.append((row, col - 1))
                q.append((row, col + 1))
            islands_count += 1
    return islands_count


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

    def test_my_bfs(self):
        for m, expected in self.TEST_CASES:
            self.assertEqual(expected, my_bfs(m))