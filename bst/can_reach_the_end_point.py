import unittest
import collections
from typing import List
from copy import deepcopy


class MyPoint:
    def __init__(self, x, y, dx=None, dy=None):
        # 表示某个决策的出发点
        self.x = x
        self.y = y
        # (dx, dy)的组合表示方向向量, 上下左右分别是(0,-1),(0,1),(-1,0),(1,0)
        self.dx = dx
        self.dy = dy


# noinspection PyShadowingBuiltins
def backtrace_solution(map: List[List[int]]) -> bool:
    """
    类似N皇后问题的「决策+回溯」算法
    1. 不能走回头路
    2. 避免陷入环形路径的死循环(原地转圈圈)
    通过seen = {(0, 0)}记录已访问过的节点，同时解决1和2
    """
    decisions = collections.deque([
        MyPoint(x=0, y=0, dx=1, dy=0),
        MyPoint(x=0, y=0, dx=0, dy=1)
    ])
    max_x = len(map[0]) - 1
    max_y = len(map) - 1
    seen = {(0, 0)}
    while decisions:
        decision = decisions.popleft()
        next_point = MyPoint(x=decision.x + decision.dx, y=decision.y + decision.dy)
        # print("From", (decision.x, decision.y), "To", (next_point.x, next_point.y))
        if (next_point.x, next_point.y) in seen:
            continue
        # 如果遇到障碍物(next_point的值为0)
        if map[next_point.x][next_point.y] == 0:
            # 通过seen记忆已经访问过的节点，防止走环形导致死循环
            seen.add((next_point.x, next_point.y))
            continue
        if map[next_point.x][next_point.y] == 9:
            return True

        directions = []
        if next_point.x == 0:
            directions.append((1, 0))
        elif 0 < next_point.x < max_x:
            directions.append((1, 0))
            directions.append((-1, 0))
        else:
            directions.append((-1, 0))

        if next_point.y == 0:
            directions.append((0, 1))
        elif 0 < next_point.y < max_y:
            directions.append((0, 1))
            directions.append((0, -1))
        else:
            directions.append((0, -1))
        # 不能走回头路，但是不排除有环形走死循环的可能，所以还是要seen存储已访问的节点
        for dx, dy in directions:
            decisions.append(MyPoint(next_point.x, next_point.y, dx, dy))
        # 通过seen记忆已经访问过的节点，防止走环形导致死循环
        # directions.remove((-decision.dx, -decision.dy))
        seen.add((next_point.x, next_point.y))
    return False


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([
             [1, 0, 1, 1, 0, 0],
             [1, 1, 0, 0, 0, 0],
             [1, 1, 0, 1, 1, 0],
             [0, 0, 1, 0, 0, 0],
             [0, 1, 0, 1, 1, 0],
             [0, 1, 1, 0, 1, 9]
         ], False),
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
