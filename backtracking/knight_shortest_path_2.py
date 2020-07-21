import unittest
import collections
import sys
from typing import List


class DecisionOld:
    def __init__(self, x, y, dx, dy, steps=0):
        # 表示某个决策的出发点，如果前进的下一个点已被访问过或已越界则退回出发点(backtracking)
        self.x = x
        self.y = y
        # (dx, dy)的组合表示方向向量, 上下左右分别是(0,-1),(0,1),(-1,0),(1,0)
        self.dx = dx
        self.dy = dy
        # 从起点到出发点，之前一共走了多少步
        self.steps = steps


class MyPoint:
    def __init__(self, x, y, steps):
        # 表示某个决策中，马将要跳到的位置
        self.x = x
        self.y = y
        # 从起点到马将要跳到的位置，之前一共走了多少步
        self.steps = steps

    def __str__(self) -> str:
        return f"({'%2s' % self.x},{'%2s' % self.y}), steps={self.steps}"


def solution(grid: List[List[int]]) -> int:
    """
    马从矩阵左上角跳到右下角的最少跳跃次数，马只能往特定4个方向跳，而且地图中的1表示障碍物
    如果马现在的位置是(x,y)，那么马只能往以下四个位置走
    (x + 1, y + 2)
    (x - 1, y + 2)
    (x + 2, y + 1)
    (x - 2, y + 1)
    """
    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1
    min_step = sys.maxsize
    queue = collections.deque([
        MyPoint(x=1, y=2, steps=1),
        MyPoint(x=2, y=1, steps=1)
    ])
    visited = set()
    while queue:
        point = queue.popleft()
        # print(point)
        # 决策失败条件1. 如果马跳到棋盘外了
        if point.x < 0 or point.x > max_x:
            continue
        if point.y < 0 or point.y > max_y:
            continue
        # visited不会记录棋盘外的点
        visited.add((point.x, point.y))
        # 决策失败条件2. 如果马跳到障碍物
        if grid[point.x][point.y] == 1:
            continue

        # 如果马到达终点，判断是否需要更新最短步数
        if (point.x, point.y) == (max_x, max_y):
            min_step = min(min_step, point.steps)
            continue

        queue.append(MyPoint(point.x + 1, point.y + 2, point.steps + 1))
        queue.append(MyPoint(point.x - 1, point.y + 2, point.steps + 1))
        queue.append(MyPoint(point.x + 2, point.y + 1, point.steps + 1))
        queue.append(MyPoint(point.x - 2, point.y + 1, point.steps + 1))

    if min_step == sys.maxsize:
        return -1
    return min_step


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 3),
        ([[0, 1, 0],
          [0, 0, 1],
          [0, 0, 0]], -1),
    ]

    def test(self):
        for matrix, expected in self.TEST_CASES:
            self.assertEqual(expected, solution(matrix))
