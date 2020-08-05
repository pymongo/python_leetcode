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
        if dfs(next_row, next_col, visited, word_next_index + 1, word_size, word, board, n_rows, n_cols):
            return True
        visited[next_row][next_col] = False
    # return board[row][col] == word[word_next_index-1]
    return False


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


def dfs_better_helper(board, word):
    n_rows = len(board)
    n_cols = len(board[0])
    word_size = len(word)
    first_letter = word[0]
    if word_size == 1 and n_rows == 1 and n_cols == 1:
        return board[0][0] == first_letter

    for row in range(n_rows):
        for col in range(n_cols):
            if board[row][col] == first_letter:
                if dfs_better(row, col, 0, word, word_size, board, n_rows, n_cols):
                    return True
    return False


def dfs_better(
    row: int,
    col: int,
    word_index: int,
    word: str,
    word_size: int,
    board: List[List[str]],
    n_rows: int,
    n_cols: int,
):
    # 这两个判断需要连在一起，第二个if需要第一个if对下标的判断
    if word_index == word_size:
        return True
    if board[row][col] != word[word_index]:
        return False

    visited_letter = board[row][col]
    # TODO 节省了一个visited遍历的写法
    board[row][col] = '#'

    for row_offset, col_offset in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        next_row, next_col = row + row_offset, col + col_offset
        if not (0 <= next_row < n_rows and 0 <= next_col < n_cols):
            continue
        if dfs_better(next_row, next_col, word_index + 1, word, word_size, board, n_rows, n_cols):
            return True

    board[row][col] = visited_letter

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

    def test_dfs2(self):
        for board, word, is_exists_in_grid in self.TEST_CASES:
            print(word)
            self.assertEqual(is_exists_in_grid, dfs_better_helper(board, word))
