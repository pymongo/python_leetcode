import unittest
import collections
from typing import List


def dfs(
    row: int,
    col: int,
    visited: List[List[bool]],
    word_next_index: int,
    word_size: int,
    word: str,
    board: List[List[str]],
    n_rows: int,
    n_cols: int,
) -> bool:
    if word_next_index == word_size:
        return True
    for delta_row, delta_col in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        next_row, next_col = row + delta_row, col + delta_col
        if not (0 <= next_row < n_rows and 0 <= next_col < n_cols):
            continue
        if visited[next_row][next_col]:
            continue
        if board[next_row][next_col] != word[word_next_index]:
            continue
        visited[next_row][next_col] = True
        if dfs(next_row, next_col, visited, word_next_index+1, word_size, word, board, n_rows, n_cols):
            return True
        visited[next_row][next_col] = False


def dfs_helper(board: List[List[str]], word: str) -> bool:
    n_rows = len(board)
    n_cols = len(board[0])
    visited = [[False] * n_cols for _ in range(n_rows)]
    word_size = len(word)
    if word_size == 1 and n_rows == 1 and n_cols == 1:
        return board[0][0] == word[0]
    for row in range(n_rows):
        for col in range(n_cols):
            if dfs(row, col, visited, 0, word_size, word, board, n_rows, n_cols):
                return True
    return False


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([['a']], "a", True),
        ([['a', 'a']], "aaa", False),
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

    def test_dfs(self):
        for board, word, is_exists_in_grid in self.TEST_CASES:
            print(word)
            self.assertEqual(is_exists_in_grid, dfs_helper(board, word))
