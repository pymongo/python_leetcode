import unittest
import collections
import sys
from typing import List


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


HORSE_DIRECTIONS = (
    (1, 2), (1, -2), (-1, 2), (-1, -2),
    (2, 1), (2, -1), (-2, 1), (-2, -1)
)


def my_bfs(grid: List[List[int]], source: Point, destination: Point) -> int:
    """
    给定一个grid，0表示可通过，1表示障碍物或已访问
    给定一个起点坐标，能否按国际象棋中 马的8种跳跃方向，跳到终点坐标? 找到最短路径的方案
    """
    rows = len(grid)
    cols = len(grid[0])
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
            # 如果图每条边的权重不为1，则这里可能不是最短路径
            return steps
        next_steps = steps + 1
        for dx, dy in HORSE_DIRECTIONS:
            next_x, next_y = x + dx, y + dy
            if -1 < next_x < rows and -1 < next_y < cols:
                queue.append((next_x, next_y, next_steps))
    return -1


"""
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
"""


class Solution(unittest.TestCase):
    TEST_CASES = [
        ([[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]], [2, 0], [2, 2], 2),
        ([[0, 1, 0],
          [0, 0, 1],
          [0, 0, 0]], (2, 0), (2, 2), -1),
    ]

    def test_bfs(self):
        for grid, source, dest, min_steps in self.TEST_CASES:
            self.assertEqual(min_steps, my_bfs(grid, Point(source[0], source[1]), Point(dest[0], dest[1])))

    def test_bfs_two_direction(self):
        for grid, source, dest, min_steps in self.TEST_CASES:
            self.assertEqual(min_steps, self.bfs_two_direction(grid, Point(source[0], source[1]), Point(dest[0], dest[1])))

    # 双向BFS搜索的解法
    @staticmethod
    def bfs_two_direction(grid: List[List[int]], source: Point, destination: Point) -> int:
        m = len(grid)
        if m == 0:
            return -1
        if grid[destination.x][destination.y] == 1:
            return -1
        if (source.x, source.y) == (destination.x, destination.y):
            # 双向宽度优先搜索需要特判一下起点等于终点的情况
            return 0
        n = len(grid[0])

        # source向前搜索的队列
        forward_queue = collections.deque()
        forward_queue.append((source.x, source.y))
        forward_seen = set()
        forward_seen.add((source.x, source.y))
        # destination向后搜索的队列
        backward_queue = collections.deque()
        backward_queue.append((destination.x, destination.y))
        backward_seen = set()
        backward_seen.add((destination.x, destination.y))

        distance = 0
        while forward_queue and backward_queue:
            distance += 1
            for i in range(len(forward_queue)):
                x, y = forward_queue.popleft()
                for dx, dy in HORSE_DIRECTIONS:
                    next_x, next_y = x + dx, y + dy
                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                        continue
                    if grid[next_x][next_y] == 1:
                        continue
                    if (next_x, next_y) in forward_seen:
                        continue
                    if (next_x, next_y) in backward_seen:
                        return distance
                    forward_seen.add((next_x, next_y))
                    forward_queue.append((next_x, next_y))

            distance += 1
            for i in range(len(backward_queue)):
                x, y = backward_queue.popleft()
                for dx, dy in HORSE_DIRECTIONS:
                    next_x, next_y = x + dx, y + dy
                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                        continue
                    if grid[next_x][next_y] == 1:
                        continue
                    if (next_x, next_y) in backward_seen:
                        continue
                    if (next_x, next_y) in forward_seen:
                        return distance
                    backward_seen.add((next_x, next_y))
                    backward_queue.append((next_x, next_y))

        # 如果双向搜索中没有相遇，则其中一个队列应该会搜索到尽头
        return -1
