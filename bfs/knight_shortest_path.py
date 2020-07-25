import unittest
import collections
import sys
from typing import List

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def my_bfs(grid: List[List[int]], source: Point, destination: Point) -> int:
    """
    给定一个grid，0表示可通过，1表示障碍物或已访问
    给定一个起点坐标，能否按国际象棋中 马的8种跳跃方向，跳到终点坐标? 找到最短路径的方案
    """
    rows = len(grid)
    cols = len(grid[0])
    min_steps = sys.maxsize
    queue = collections.deque()
    queue.append((source.x, source.y, 0))
    while queue:
        x, y, steps = queue.popleft()
        if not (-1 < x < rows and -1 < y < cols):
            continue
        if grid[x][y] == 1:
            continue
        grid[x][y] = 1
        if x == destination.x and y == destination.y:
            # min_steps = min(min_steps, steps)
            return min_steps
        # 优化1. 将马跳跃的方向(dx, dy)抽取为常量，将判断是否越界的代码抽取成子函数
        # 优化2. 先判断越界后加入队列，避免错误的点入栈又出栈消耗性能
        # 优化3. 可以使用distance = {(source.x, source.y): 0}存储步骤数
        queue.append((x + 1, y + 2, steps + 1))
        queue.append((x + 1, y - 2, steps + 1))
        queue.append((x - 1, y + 2, steps + 1))
        queue.append((x - 1, y - 2, steps + 1))
        queue.append((x + 2, y + 1, steps + 1))
        queue.append((x + 2, y - 1, steps + 1))
        queue.append((x - 2, y + 1, steps + 1))
        queue.append((x - 2, y - 1, steps + 1))
    if min_steps == sys.maxsize:
        return -1
    return min_steps


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]
         ], [2, 0], [2, 2], 2),
        ([
             [0, 1, 0],
             [0, 0, 1],
             [0, 0, 0]
         ], (2, 0), (2, 2), -1),
    ]

    def test(self):
        for grid, source, dest, min_steps in self.TEST_CASES:
            self.assertEqual(min_steps, my_bfs(grid, Point(source[0], source[1]), Point(dest[0], dest[1])))
