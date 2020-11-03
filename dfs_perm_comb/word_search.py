import unittest
from typing import List


class Solution(unittest.TestCase):
    TESTCASES = [
        ([['a', 'a']], "aaa", False),
        ([['a']], "a", True),
        ([
             ['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']
         ], "ABCB", False),
        ([
             ['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']
         ], "ABCCED", True),
        ([
             ['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']
         ], "SEE", True),
    ]

    def test_solution_entrance(self):
        for board, word, is_exists_in_grid in self.TESTCASES:
            print(board, word)
            self.assertEqual(is_exists_in_grid, self.solution_entrance(board, word))

    # 196 ms 击败了 92.64%
    @staticmethod
    def solution_entrance(board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        word_last_idx = len(word) - 1

        def dfs(x, y, k) -> bool:
            char = board[x][y]
            if char != word[k]:
                return False
            if k == word_last_idx:
                return True
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x2, y2 = x + dx, y + dy
                if x2 < 0 or x2 >= m or y2 < 0 or y2 >= n:
                    continue
                if board[x2][y2] == '#':
                    continue

                board[x][y] = '#'
                if dfs(x2, y2, k + 1):
                    return True
                board[x][y] = char
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
