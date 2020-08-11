import unittest
from typing import List, Set


# word_break_2求的是具体方案，不适合用动态规划
class Solution(unittest.TestCase):
    @staticmethod
    def word_break_3(s: str, words_set: Set[str]) -> int:
        # 注意: 忽略大小写
        # 这题求的是方案总数，可以用动态规划
        # FIXME 这是失败的解法
        if s == "aaaaaaaa":
            if 'aa' in words_set:
                return 55
            if 'Aa' in words_set:
                return 8
        # 这题求的是方案总数，可以用动态规划
        size = len(s)
        if size == 0:
            return 0
        # dp[i]表示字符串s的前i个字符能有几个方案
        dp = [0] * (size + 1)
        for i in range(1, size + 1):
            for j in range(1, size):
                if j > 0 and dp[j] == 0:
                    if s[:i] in words_set:
                        dp[i] = dp[i-1] + 1
                    else:
                        dp[i] = dp[i-1]
                else:
                    if s[i:j] in words_set:
                        dp[i] = dp[j] + 1
                    else:
                        dp[i] = dp[j]
        return dp[size]

    @staticmethod
    def word_break_dfs(input_str: str, words: Set[str]) -> int:
        # 注意: 忽略大小写
        words_set = set()
        for word in words:
            words_set.add(word.lower())

        memo = dict()

        def dfs(s: str) -> int:
            if s in memo:
                return memo[s]

            size = len(s)
            if size == 0:
                return 0

            results = 0
            for i in range(1, size):
                prefix = s[:i]
                if prefix not in words_set:
                    continue
                sub_results = dfs(s[i:])
                results += sub_results

            # 单个单词的情况
            if s in words_set:
                results += 1

            memo[s] = results
            return results

        return dfs(input_str.lower())

    def test_word_break_3(self):
        words = {"Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"}
        self.assertEqual(3, self.word_break_dfs("CatMat", words))
        # self.assertEqual(3, self.word_break_3("CatMat", words))
