import unittest
from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic,PyPep8Naming
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 更优的做法是字典树
        # dp[i] 表示字符串 s 前 i 个字符组成的字符串 s[0:0..=i-1] 能否被字典中的单词填充
        words_set = set(wordDict)
        size = len(s)
        dp = [False] * (size + 1)
        dp[0] = True
        for i in range(1, size + 1):
            for j in range(0, i):
                # 注意dp[i]表示从0到i-1的子串
                # 所以dp[j]表示s[0:j]可被划分，再加上s[j:i]也能被划分，那么从0到i-1的子串dp[i]也能被划分
                if dp[j] and s[j:i] in words_set:
                    dp[i] = True
                    continue
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
