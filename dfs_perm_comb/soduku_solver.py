import unittest
from typing import List


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
        ([["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
         [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
          ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
          ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
          ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
          ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
          ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
          ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
          ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
          ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
         )
    ]

    def test(self):
        for board, expected in self.TEST_CASES:
            self.f(board)
            self.assertListEqual(expected, board)

    @staticmethod
    def f(board: List[List[str]]):
        used = SodukuUsed()
        Solution.init_board_used(board, used)
        Solution.dfs(0, used, board)

    @staticmethod
    def init_board_used(board: List[List[str]], used: SodukuUsed):
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                used.rows[i].add(val)
                used.cols[j].add(val)
                used.boxs[(i // 3) * 3 + j // 3].add(val)

    @staticmethod
    def dfs(index: int, used: SodukuUsed, board: List[List[str]]) -> bool:
        if index == 81:
            return True

        i, j = index // 9, index % 9
        if board[i][j] != '.':
            # 如果当前位置不为空，则去找下一个位置去填数
            return Solution.dfs(index + 1, used, board)

        for val in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            if val in used.rows[i]:
                continue
            if val in used.cols[j]:
                continue
            box_index = i // 3 * 3 + j // 3
            if val in used.boxs[box_index]:
                continue

            used.rows[i].add(val)
            used.cols[j].add(val)
            used.boxs[box_index].add(val)
            board[i][j] = val

            if Solution.dfs(index + 1, used, board):
                return True

            used.rows[i].remove(val)
            used.cols[j].remove(val)
            used.boxs[box_index].remove(val)
            board[i][j] = '.'

        return False
