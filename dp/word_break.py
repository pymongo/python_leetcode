import unittest
from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic,PyPep8Naming
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 更优的做法是Trie字典树
        # dp[i] 表示字符串 s 前 i 个字符组成的字符串 s[0:0..=i-1] 能否被字典中的单词填充
        words_set = set(wordDict)
        size = len(s)
        dp = [False] * (size + 1)
        dp[0] = True
        for i in range(1, size + 1):
            for j in range(0, i):
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
            for j in range(1, max_word_length+1):
                if j > i:
                    break
                # 注意这里for的是s[i-j..=i-1:i]之间的所有子串，有点像从终点往左看每个子串
                # 还是jump-game那样正常顺序好理解，穷举0到i-1，看看过去的点中有没有一个点到现在单词的子串在字典里
                if dp[i-j] and s[i-j:i] in words_set:
                    dp[i] = True
                    break
        return dp[size]


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ]

    def test_word_break(self):
        solution = Solution()
        for s, words, expected in self.TEST_CASES:
            self.assertEqual(expected, solution.wordBreak(s, words))
