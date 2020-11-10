import unittest
from typing import List, Dict, Union


def dfs(
    row: int,
    col: int,
    row_size: int,
    col_size: int,
    board: List[List[str]],
    parent_node: Dict[str, Union[Dict, str]],
    matched_words: List[str],
    words: List[str]
) -> bool:
    letter = board[row][col]
    # market curr letter is visited, make board[new_row][new_col] not in curr_node in inner dfs_search
    board[row][col] = '#'
    curr_node = parent_node[letter]
    word_match = curr_node.pop('$', False)  # if key not exist return False
    if isinstance(word_match, str):
        word_match_rev = reversed(word_match)
        word_size = len(word_match)
        better_solution = []
        better_solution_cnt = 0
        # 如果当前找到的是adee，但是可以有更优的da+ee两个方案，则抛弃当前方案
        for word in words:
            if len(word) < word_size:
                if word in word_match or word in word_match_rev:
                    better_solution_cnt += 1
                    if better_solution_cnt >= 2:
                        return False

        # 如果找到某个单词了，说明当前路径上的所有字母都已用过，提前return
        matched_words.append(word_match)
        return True

    for row_offset, col_offset in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_row, new_col = row + row_offset, col + col_offset
        if not (0 <= new_row < row_size and 0 <= new_col < col_size):
            continue
        if board[new_row][new_col] == '#':
            continue
        if board[new_row][new_col] not in curr_node:
            continue
        if dfs(new_row, new_col, row_size, col_size, board, curr_node, matched_words, words):
            # 先不剪枝
            # if not curr_node:
            #     parent_node.pop(letter)
            return True

    # 如果没找到则回溯(将棋盘中的visited标回letter)
    board[row][col] = letter


# [LOCK]https://lintcode.com/problem/boggle-game/
# 与word_search_2的区别是矩阵中的每个字母只能使用一次，而且返回的是最多单词被圈中的数量
# 一定要优先匹配前缀树中较短的单词，才能尽可能多地匹配
# FIXME 例如第三行是\['a', 'd', 'e', 'e']的测试用例，总是匹配成adee而不是更优的da+ee，都不知道该怎么设计才能优先匹配较短的字符串，或者发现更优方案，抛弃之前的答案
# FIXME 已抛弃该问题: 这道题是Airbnb版的Boggle game。 已经不考了。临场写出来真的不太现实。建议不用准备了。
# TODO 本题已ABANDONED(放弃)
def word_search_3(board: List[List[str]], words: List[str]) -> int:
    trie = {}
    for word in words:
        curr_node = trie
        for letter in word:
            # or curr_node = curr_node.setdefault(letter, {})
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        # Mark end of word and store whole word
        curr_node['$'] = word
    print(trie)

    matched_words = []
    row_size = len(board)
    col_size = len(board[0])
    for row in range(row_size):
        for col in range(col_size):
            letter = board[row][col]
            if letter == '#':
                continue
            if letter in trie:
                dfs(row, col, row_size, col_size, board, trie, matched_words, words)
    print(matched_words)
    return len(matched_words)


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([
             ['a', 'b', 'c', 'e'],
             ['s', 'f', 'c', 's'],
             ['a', 'd', 'e', 'e'],
         ],
         ["as", "ab", "cf", "da", "ee", "e", "adee", "eeda"],
         5
        ),
        ([
             ['d', 'o', 'a', 'f'],
             ['a', 'g', 'a', 'i'],
             ['d', 'c', 'a', 'n']
         ],
         ["dog", "dad", "dgdg", "can", "again"],
         # dad/dog, can
         2),
        ([
             ['a', 'b', 'c', 'e'],
             ['s', 'f', 'e', 's'],
             ['a', 'd', 'e', 'e'],
         ],
         ["abceseeefs", "abceseedasfe"],
         1
        )
    ]

    def test(self):
        for board, words, expected in self.TEST_CASES:
            self.assertEqual(expected, word_search_3(board, words))
