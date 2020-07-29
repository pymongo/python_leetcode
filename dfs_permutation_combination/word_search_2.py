# Boggle单词游戏, 给你一个乱序的字母矩阵，从矩阵中任意一点往上下左右四个方向去搜索，能找到几个单词
import unittest
from typing import List, Dict, Union


def dfs_search(
    row: int,
    col: int,
    row_size: int,
    col_size: int,
    board: List[List[str]],
    parent_node: Dict[str, Union[Dict, str]],
    matched_words: List[str]
):
    # 临时存储当前坐标的letter，用于回溯
    letter = board[row][col]
    curr_node = parent_node[letter]
    word_match = curr_node.pop('$', False)  # if key not exist return False
    if word_match:
        matched_words.append(word_match)
    # market curr letter is visited, make board[new_row][new_col] not in curr_node in inner dfs_search
    board[row][col] = '#'

    for row_offset, col_offset in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_row, new_col = row + row_offset, col + col_offset
        if not (0 <= new_row < row_size and 0 <= new_col < col_size):
            continue
        if board[new_row][new_col] not in curr_node:
            continue
        dfs_search(new_row, new_col, row_size, col_size, board, curr_node, matched_words)

    # backtracking
    board[row][col] = letter
    # Optimization: incrementally remove the matched leaf node in Trie.
    if not curr_node:
        # 单词的最末尾节点(叶子节点)必为 {'$': 'apple'}
        # 所以之前curr_node.pop('$', False)执行后，curr_node必为空{}
        # 一个单词已被选中添加到results后，会逐层往上「✂️枝」，最终前缀树的trie中会去掉这层单词路径
        # 去重的重要步骤，去掉前缀树中以访问过的单词的最末尾字符
        parent_node.pop(letter)


def boggle(board: List[List[str]], words: List[str]) -> List[str]:
    # 构建前缀树, 具体原理请看: [Implement Trie (Prefix Tree)]这题
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

    matched_words = []
    row_size = len(board)
    col_size = len(board[0])
    for row in range(row_size):
        for col in range(col_size):
            if board[row][col] in trie:
                dfs_search(row, col, row_size, col_size, board, trie, matched_words)
    return matched_words


class Testing(unittest.TestCase):
    TEST_CASES = [
        (["oath", "pea", "eat", "rain"],
         [
             ['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']
         ],
         ["eat", "oath"]
         ),
        (["aaaa"],
         [
             ['a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a']
         ],
         ["aaaa"]
         ),
    ]

    def test(self):
        for words, board, matched_words in self.TEST_CASES:
            self.assertCountEqual(matched_words, boggle(board, words))
