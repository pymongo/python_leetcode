import unittest
from typing import List


class Solution(unittest.TestCase):
    TEST_CASES = [
        ("lintcode", ["de", "ding", "co", "code", "lint"], ["lint code", "lint co de"])
    ]

    def test(self):
        for s, words, results in self.TEST_CASES:
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
