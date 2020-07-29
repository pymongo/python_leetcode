"""
前缀树每个节点只有一个字符，root相当于一个dummyHead不存储字符
每个节点除了要存储字符，还要存储从根到当前节点是否构成一个单词
TODO 这题没要求实现「删除操作」，所以可以不写析构函数，较简单

## 前缀树的优点
插入和查找的时间复杂度都是O(L), L为单词长度

## 前缀树的应用
1. 搜索框自动补全或提供下拉选项的提示，例如谷歌搜索rust，下面会有很多rust开头的候选词的提示
2. 9宫格/9键手机输入时，联想候选词
3. Typo/拼写检查
4. Boggle单词游戏, 给你一个乱序的字母矩阵，从矩阵中任意一点往上下左右四个方向去搜索，能找到几个单词
5. IP 路由 (最长前缀匹配)
"""

import unittest
from typing import List, Optional


class TreeNode:
    """
    Python中可以通过 .__sizeof__ 或 sys.getsizeof 获取对象占内存多少个字节，Ruby则没法获取对象占内存的大小
    sys.getsizeof(None) # 16
    False.__sizeof__() # 24
    True.__sizeof__() # 28
    Python中空指针None占据内存空间大小比Boolean类型还小
    我还以为True和False和None都是操作系统内存最小单位 1Byte的大小
    """
    def __init__(self, char: str = "", is_word: bool = False):
        self.char = char
        self.is_word = is_word
        self.children: List[Optional[TreeNode]] = [None] * 26


# prefix tree
class Trie:

    def __init__(self):
        self.root: TreeNode = TreeNode()

    def insert(self, word: str) -> None:
        if not word:
            return
        curr_node = self.root
        for letter in word:
            char_ascii = ord(letter) - 98
            if curr_node.children[char_ascii] is None:
                curr_node.children[char_ascii] = TreeNode(letter)
            curr_node = curr_node.children[char_ascii]

        curr_node.is_word = True

    def search(self, word: str) -> bool:
        curr_node = self._search_prefix(word)
        return curr_node is not None and curr_node.is_word

    # noinspection PyPep8Naming
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._search_prefix(prefix) is not None

    def _search_prefix(self, word: str) -> Optional[TreeNode]:
        """
        Returns last char of word in the trie
        """
        if not word:
            return None
        curr_node = self.root
        for letter in word:
            char_ascii = ord(letter) - 98
            if curr_node.children[char_ascii] is None:
                return None
            curr_node = curr_node.children[char_ascii]
        return curr_node


# 用HashMap实现的Prefix Tree比数组的实现快2倍以上
class TrieHashMap1:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        # $ means is_word
        curr_node['$'] = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        if '$' not in curr_node:
            return False
        return True

    # noinspection PyPep8Naming
    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char not in curr_node:
                return False
            curr_node = curr_node[char]
        return True


class Testing(unittest.TestCase):
    def test_1(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))

    def test_2(self):
        """
        leetcode用eval运行单元测试，我就不太会
        ["Trie", "insert" , "search", "search"  , "search" , "startsWith", "startsWith", "startsWith"]
        [[]    , ["hello"], ["hell"], ["helloa"], ["hello"], ["hell"]    , ["helloa"]  , ["hello"]]
        [null  , null     , false   , false     , true     , true        , false       , true]
        """
        trie = Trie()
        trie.insert("hello")
        self.assertFalse(trie.search("hell"))
        self.assertFalse(trie.search("hell"))
        self.assertFalse(trie.search("helloa"))
        self.assertTrue(trie.search("hello"))
        self.assertTrue(trie.startsWith("hell"))
        self.assertFalse(trie.startsWith("helloa"))
        self.assertTrue(trie.startsWith("hello"))

    def test_tire_hash_map_1(self):
        trie = TrieHashMap1()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))
