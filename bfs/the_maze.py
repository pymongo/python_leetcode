import unittest
from typing import List
import collections


# maze就是迷宫的意思
class Solution(unittest.TestCase):
    TESTCASES = [
        ([[0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0],
          [1, 1, 0, 1, 1],
          [0, 0, 0, 0, 0]
          ], [0, 4], [4, 4], True),
    ]

    def test(self):
        for grid, start, dest, can_reach in self.TESTCASES:
            self.assertEqual(can_reach, self.f(grid, start, dest))

    @staticmethod
    def f(grid: List[List[int]], start: List[int], dest: List[int]) -> bool:
        # 题目已给出信息，起点和终点不相同，而且棋盘不为空
        # TODO 这题的难点在于，必须要碰到边界或障碍物才能换方向
        m, n = len(grid), len(grid[0])
        end_x, end_y = dest[0], dest[1]

        q = collections.deque()
        q.append((start[0], start[1]))
        while q:
            x, y = q.popleft()
            if (x, y) == (end_x, end_y):
                return True
            # mark current point as visited
            grid[x][y] = 2
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                next_x, next_y = x + dx, y + dy
                # 一直往前走直到遇到障碍物或边界
                while 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] != 1:
                    next_x, next_y = next_x + dx, next_y + dy
                # 跳出循环时必越界或撞墙，需要回退一步
                next_x, next_y = next_x - dx, next_y - dy
                if grid[next_x][next_y] == 0:
                    q.append((next_x, next_y))
        return False

        # def search(queue, visited, opposite_visited) -> bool:
        #     x, y, dx, dy = queue.popleft()
        #     next_x, next_y = x + dx, y + dy
        #     if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or grid[next_x][next_y] == 1:
        #         # 需要换方向
        #         for new_dx, new_dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        #             if (new_dx, new_dy) == (dx, dy):
        #                 continue
        #             next_x, next_y = x+new_dx, y+next_y
        #             if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or grid[next_x][next_y] == 1:
        #                 continue
        #             if (next_x, next_y) in opposite_visited:
        #                 return True
        #             visited.add((next_x, next_y))
        #             queue.append((next_x, next_y, new_dx, new_dy))
        #         return False
        #     # 继续往前走的情况
        #     if (next_x, next_y) in opposite_visited:
        #         return True
        #     visited.add((next_x, next_y))
        #     return False
        #
        # for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        #     next_x, next_y = x + dx, y + dy
        #     if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
        #         continue
        #     if grid[next_x][next_y] == 1:
        #         continue
        #     if (next_x, next_y) in visited:
        #         continue
        #     if (next_x, next_y) in opposite_visited:
        #         return True
        #     queue.append((next_x, next_y))
        # return False

        # while start_q and end_q:
        #     if search(start_q, start_seen, end_seen):
        #         return True
        #
        #     if search(end_q, end_seen, start_seen):
        #         return True
        # return False
