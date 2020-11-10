"""
周赛#205 第一题: https://leetcode-cn.com/contest/weekly-contest-205/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
"""
import unittest
from typing import List


class Solution(unittest.TestCase):
    def test(self):
        TEST_CASESs = [
            ("aabaa", [1, 2, 3, 4, 1], 2),
            ("abaac", [1, 2, 3, 4, 5], 3),
            ("abc", [1, 2, 3], 0),
        ]
        for s, cost, expected in TEST_CASESs:
            self.assertEqual(expected, self.f(s, cost))

    # 周赛第三题
    @staticmethod
    def f(s: str, cost: List[int]) -> int:
        n = len(cost)
        if n <= 1:
            return 0
        res = 0
        i = 1
        while i < n:
            if s[i] == s[i - 1]:
                j = i
                # 找到连续的一片重复字母
                while j < n and s[j] == s[j - 1]:
                    j += 1
                res += sum(cost[i - 1:j]) - max(cost[i - 1:j])
                i = j
            else:
                i += 1
        return res
