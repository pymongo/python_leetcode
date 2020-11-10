import unittest
from typing import List


class Solution(unittest.TestCase):
    TEST_CASES = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
    ]

    def test(self):
        for strs, output in self.TEST_CASES:
            self.assertEqual(output, self.f(strs))

    @staticmethod
    def f(strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""

        def lcp(str1: str, str2: str) -> str:
            res = ""
            j = 0
            for i in range(min(len(str1), len(str2))):
                if str1[i] != str2[j]:
                    break
                res += str1[i]
                j += 1
            return res

        interval = 1
        while interval < n:
            for k in range(0, n - interval, interval):
                strs[k] = lcp(strs[k], strs[k + interval])
            interval *= 2
        return strs[0]
