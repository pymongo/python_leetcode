import unittest
from typing import List, Set


# word_break_2求的是具体方案，不适合用动态规划
class Solution(unittest.TestCase):
    TESTCASES = [
        ("lintcode", ["de", "ding", "co", "code", "lint"], ["lint code", "lint co de"])
    ]

    def test(self):
        for s, words, results in self.TESTCASES:
            self.assertCountEqual(results, self.find(s, words))

    @staticmethod
    def find(input_str: str, words: List[str]) -> List[str]:
        if not words:
            return []
        words_set = set(words)
        memo = dict()

        def dfs(s: str) -> List[str]:
            if s in memo:
                return memo[s]

            size = len(s)
            if size == 0:
                return []

            results = []
            for i in range(1, size):
                prefix = s[:i]
                if prefix not in words_set:
                    continue
                sub_results = dfs(s[i:])
                for sub_result in sub_results:
                    results.append(f"{prefix} {sub_result}")

            # 单个单词的情况
            if s in words_set:
                results.append(s)

            memo[s] = results
            return results

        return dfs(input_str)
