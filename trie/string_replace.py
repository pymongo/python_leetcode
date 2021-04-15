import unittest
from typing import List


class TireNode:
    def __init__(self):
        self.children = {}
        # replacement表示从根节点到当前节点组成的字符串(在数组A中)，能替换成数组B的哪个字符串
        self.replacement = None


class Tire:
    def __init__(self):
        self.root = TireNode()

    def insert(self, word: str, replacement: str):
        curr = self.root
        for char in word:
            # Insert key with a value of default if key is not in the dictionary.
            # Return the value for key if key is in the dictionary, else default.
            curr = curr.children.setdefault(char, TireNode())
        curr.replacement = replacement

    def search(self, word: str) -> str:
        curr, replacement = self.root, None
        for char in word:
            if char not in curr.children:
                break
            curr = curr.children[char]
            # 不断搜索字典树，找到新的(更长的replacement)就更新
            if curr.replacement is not None:
                replacement = curr.replacement

        # 如果没找到，就返回第一个字符，让字符串S原封不动地替换下一个字符，然后指针会后移一位
        if replacement is None:
            replacement = word[0]
        return replacement


class Solution(unittest.TestCase):
    TEST_CASES = [
        # ababa -> cccba -> cccba
        # ^           ^         ^
        (["ab", "aba"], ["cc", "ccc"], "ababa", "cccba"),
    ]

    def test(self):
        for a, b, s, after_replace in self.TEST_CASES:
            self.assertEqual(after_replace, self.f(a, b, s))

    @staticmethod
    def f(a: List[str], b: List[str], s: str) -> str:
        if not a or not b:
            return s

        tire = Tire()
        for i, word in enumerate(a):
            # 只有word是s的子串其才会被放到trie中, 这样就保证了每次search的时候, 每次匹配s[i]做的都是有用功
            if word in s:
                tire.insert(word, b[i])

        result = ""
        while s:
            replacement = tire.search(s)
            print(replacement)
            result += replacement
            s = s[len(replacement):]

        return result
