import unittest
from typing import List


# 关键词: 完全背包、分词法、前缀型、划分型
class Solution(unittest.TestCase):
    TESTCASES = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ]

    def test_word_break_backpack(self):
        for s, words, expected in self.TESTCASES:
            self.assertEqual(expected, Solution.word_break_backpack(s, words))

    @staticmethod
    def word_break_backpack(s: str, words: List[str]) -> bool:
        """
        将本题抽象成完全背包问题的思路
        与coin_exchange一样，本题也是可以从一堆单词中选任意个
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        # 这里只能先遍历i，再遍历words
        for i in range(1, n + 1):
            for word in words:
                word_len = len(word)
                if i >= word_len and s[i - word_len:i] == word:
                    dp[i] = dp[i] or dp[i - word_len]
        return dp[n]

    def test_word_break(self):
        for s, words, expected in self.TESTCASES:
            self.assertEqual(expected, Solution.wordBreak(s, words))

    # noinspection PyPep8Naming
    @staticmethod
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        # 更优的做法是Trie字典树
        # dp[i] 表示字符串 s 前 i 个字符组成的字符串 s[0:0..=i-1] 能否被字典中的单词填充
        words_set = set()
        max_word_len = 0
        for word in wordDict:
            max_word_len = max(max_word_len, len(word))
            words_set.add(word)
        size = len(s)
        dp = [False] * (size + 1)
        dp[0] = True
        for i in range(1, size + 1):
            # 如果i很长，没必要让j从0遍历到i，实际上只需要考虑最大单词长度即可
            # for j in range(0, i):
            for j in range(max(0, i - max_word_len), i):
                # 注意dp[i]表示从0到i-1的子串
                # 如果s[0:j]可被划分，而且s[j:i]也能被划分，那么从0到i-1的子串dp[i]也能被划分
                if dp[j] and s[j:i] in words_set:
                    dp[i] = True
                    continue
        return dp[size]

    @staticmethod
    def dp_state_2(s: str, words: List[str]) -> bool:
        size = 0
        words_set = set()
        # 利用单词列表中最长长度单词的优化策略
        # 从终点往左看的DP思路
        max_word_length = 0
        for word in words:
            words_set.add(word)
            size += 1
            max_word_length = max(max_word_length, len(word))

        size = len(s)
        dp = [False] * (size + 1)
        dp[0] = True
        for i in range(1, size + 1):
            for j in range(1, max_word_length + 1):
                if j > i:
                    break
                # 注意这里for的是s[i-j..=i-1:i]之间的所有子串，有点像从终点往左看每个子串
                # 还是jump-game那样正常顺序好理解，穷举0到i-1，看看过去的点中有没有一个点到现在单词的子串在字典里
                if dp[i - j] and s[i - j:i] in words_set:
                    dp[i] = True
                    break
        return dp[size]
