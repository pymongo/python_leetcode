import unittest
import collections
from typing import List
from copy import deepcopy


class MyPoint:
    def __init__(self, x, y, dx=None, dy=None):
        # 表示某个决策的出发点
        self.x = x
        self.y = y
        # (dx, dy)的组合表示方向向量, 上下左右分别是(0,1),(0,-1),(-1,0),(1,0)
        self.dx = dx
        self.dy = dy


# noinspection PyShadowingBuiltins
def backtrace_solution(map: List[List[int]]) -> bool:
    # temp = []
    # if map[0][1] == 1:
    #     temp.append(MyPoint(x=0, y=0, dx=1, dy=0))
    # if map[1][0] == 1:
    #     pass
    # if not temp:
    #     return False
    q = collections.deque([
        MyPoint(x=0, y=0, dx=1, dy=0),
        MyPoint(x=0, y=0, dx=0, dy=1)
    ])
    max_x = len(map[0]) - 1
    max_y = len(map) - 1
    while q:
        curr_point = q.popleft()
        next_point = MyPoint(x=curr_point.x + curr_point.dx, y=curr_point.y + curr_point.dy)
        # 如果遇到障碍物(next_point的值为0)
        if map[next_point.x][next_point.y] == 0:
            continue
        if map[next_point.x][next_point.y] == 9:
            return True

        last_direction = (curr_point.dx, curr_point.dy)
        directions = []
        if next_point.x == 0:
            # 不能走回头路
            if last_direction != (-1, 0):
                directions.append((1, 0))
        if 0 < next_point.x < max_x:
            if last_direction != (-1, 0):
                directions.append((1, 0))
            if last_direction != (1, 0):
                directions.append((-1, 0))
        if next_point.x == max_x:
            if last_direction != (1, 0):
                directions.append((-1, 0))

        if next_point.y == 0:
            if last_direction != (0, -1):
                directions.append((0, 1))
        if 0 < next_point.y < max_y:
            if last_direction != (0, -1):
                directions.append((0, 1))
            if last_direction != (0, 1):
                directions.append((0, -1))
        if next_point.y == max_y:
            if last_direction != (0, 1):
                directions.append((0, -1))
        for dx, dy in directions:
            q.append(MyPoint(next_point.x, next_point.y, dx, dy))
    return False


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([
             [1, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 1, 0, 0],
             [1, 1, 1, 9]
         ], True),
        ([
             [1, 1, 1],
             [1, 1, 1],
             [1, 1, 9]
         ], True),
        ([
             [1, 1, 1],
             [1, 0, 0],
             [1, 0, 9]
         ], False),
    ]

    def test(self):
        for labyrinth, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, backtrace_solution(labyrinth))
