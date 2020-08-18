import unittest
from typing import List
import collections


# maze就是迷宫的意思
class Solution(unittest.TestCase):
    TEST_CASES = [
        ([[0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0],
          [1, 1, 0, 1, 1],
          [0, 0, 0, 0, 0]
          ], [0, 4], [4, 4], True),
    ]

    def test(self):
        for grid, start, dest, can_reach in self.TEST_CASES:
            self.assertEqual(can_reach, self.f(grid, start, dest))

    @staticmethod
    def f(grid: List[List[int]], start: List[int], dest: List[int]) -> bool:
        # 题目已给出信息，起点和终点不相同
        # TODO 这题的难点在于，必须要碰到边界或障碍物才能换方向
        m = len(grid)
        if m == 0:
            return False
        n = len(grid[0])
        end_x, end_y = dest[0], dest[1]
        # if grid[end_x][end_y] == 1:
        #     return False
        start_x, start_y = start[0], start[1]

        start_q = collections.deque()
        start_seen = set()
        end_q = collections.deque()
        end_seen = set()
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            start_q.append((start_x, start_y, dx, dy))
            end_q.append((end_x, end_y, dx, dy))
            start_seen.add((start_x, start_y))
            end_seen.add((end_x, end_y))

        def search(queue, visited, opposite_visited) -> bool:
            x, y, dx, dy = queue.popleft()
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or grid[next_x][next_y] == 1:
                # 需要换方向
                for new_dx, new_dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    if (new_dx, new_dy) == (dx, dy):
                        continue
                    next_x, next_y = x+new_dx, y+next_y
                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or grid[next_x][next_y] == 1:
                        continue
                    if (next_x, next_y) in opposite_visited:
                        return True
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y, new_dx, new_dy))
                return False
            # 继续往前走的情况
            if (next_x, next_y) in opposite_visited:
                return True
            visited.add((next_x, next_y))
            return False
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

        while start_q and end_q:
            if search(start_q, start_seen, end_seen):
                return True

            if search(end_q, end_seen, start_seen):
                return True
        return False
