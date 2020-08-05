import unittest
import collections
from typing import List


def dfs(
    row: int,
    col: int,
    # word_next_index
    word_index: int,
    word_size: int,
    word: str,
    board: List[List[str]],
    n_rows: int,
    n_cols: int,
) -> bool:
    pass


def dfs_helper(board: List[List[str]], word: str) -> bool:
    n_rows = len(board)
    n_cols = len(board[0])
    visited = [[False] * n_cols for _ in range(n_rows)]
    first_letter = word[0]
    word_size = len(word)
    last_word_index = word_size - 1
    last_match_word = word[word_size-1]
    queue = collections.deque()
    for row in range(n_rows):
        for col in range(n_cols):
            if board[row][col] != first_letter:
                continue
            if visited[row][col]:
                continue
            queue.append((row, col))
            visited[row][col] = True
            word_index = 1
            while queue:
                x, y = queue.pop()
                next_match_letter = word[word_index]
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    next_x, next_y = x + dx, y + dy
                    if not (0 <= next_x < n_rows and 0 <= next_y < n_cols):
                        continue
                    if visited[next_x][next_y]:
                        continue
                    visited[next_x][next_y] = True
                    if board[next_x][next_y] != next_match_letter:
                        continue
                    if word_index == last_word_index:
                        return True
                    queue.append((next_x, next_y))
                if word_index < last_word_index:
                    word_index += 1
    return False


class Testing(unittest.TestCase):
    TEST_CASES = [
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
