import unittest
from typing import List


# 可以认为题目给的数独矩阵就是固定9x9的大小
class SodukuUsed:
    def __init__(self):
        self.rows, self.cols, self.boxs = [], [], []
        for _ in range(9):
            self.rows.append(set())
            self.cols.append(set())
            # box表示一个九宫格
            self.boxs.append(set())


class Solution(unittest.TestCase):
    TEST_CASES = [
        ([
             ["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]
         ], True),
        ([
             ["8", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]
         ], False),
    ]

    def test(self):
        for board, is_valid in self.TEST_CASES:
            self.assertEqual(is_valid, self.f(board))

    @staticmethod
    def f(board: List[List[str]]) -> bool:
        # 本题难点在于判断i和j落入了哪一个九宫格
        used = SodukuUsed()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val in used.rows[i]:
                    return False
                if val in used.cols[j]:
                    return False
                # for i in range(9): print(i // 3 * 3)
                # 0 0 0 3 3 3 6 6 6
                box_index = (i // 3) * 3 + j // 3
                if val in used.boxs[box_index]:
                    return False
                used.rows[i].add(val)
                used.cols[j].add(val)
                used.boxs[box_index].add(val)

        return True
