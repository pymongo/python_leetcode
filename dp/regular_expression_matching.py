"""
这题跟wildcard_matching不同的是，星号的含义不同
c*表示可以匹配任意个c
".*" 表示可匹配零个或多个（'*'）任意字符（'.'）
ab可以被".*"匹配

这题最快解法应该是「有限状态机/自动机」
"""
import unittest
from typing import List


class Solution:
    @staticmethod
    def re(s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 空的source字符串可以被空的pattern匹配上
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # [
        # [True, False, True],
        # [False, True, True],
        # [False, False, True]
        # ]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        # dp[i][j-2]  : a* counts as empty
                        # dp[i-1][j-2]: a* counts as single a
                        # dp[i-1][j]  : a* counts as multiple a
                        print("if p[j - 2] == s[i - 1] or p[j-2] == '.'")
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
                    else:
                        # 由于s[i]和s[j]不一样，所以只有*不选的情况, dp[i][j-1]表示*不选的情况, 与wildcard不同的是，星号不选则表示星号前面的字母也不选
                        print("dp[i][j] = dp[i][j - 2]")
                        dp[i][j] = dp[i][j - 2]
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    print("if p[j - 1] == s[i - 1] or p[j-1] == '.'")
                    dp[i][j] = dp[i - 1][j - 1]
        print(dp)
        return dp[m][n]

    @staticmethod
    def tmp(s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # s 为空串
        for j in range(1, n + 1):
            # 若 p 的第 j 个字符 p[j - 1] 是 '*'
            # 说明第 j - 1、j 位可有可无
            # 那么如果前 j - 2 个已经匹配上，前 j 个也可以匹配上
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j-1] == '.':
                    print("if p[j - 1] == s[i - 1] or p[j-1] == '.'")
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # if p[j - 2] in {s[i - 1], '.'}:
                    if p[j - 2] == s[i - 1] or p[j-2] == '.':
                        print("if p[j - 2] == s[i - 1] or p[j-2] == '.'")
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
                    else:
                        print("dp[i][j] = dp[i][j - 2]")
                        dp[i][j] = dp[i][j - 2]
        print(dp)
        return dp[m][n]


class Testing(unittest.TestCase):
    TEST_CASES = [
        # ("aa", "a", False),
        ("aa", "a*", True),
        # ("ab", ".*", True),
        # ("aab", "c*a*b", True),
        # ("mississippi", "mis*is*p*.", False),
    ]

    def test_re(self):
        for s, p, is_match in self.TEST_CASES:
            self.assertEqual(is_match, Solution.tmp(s, p))
        print(111111111)
        for source, pattern, is_match in self.TEST_CASES:
            print(source, pattern)
            self.assertEqual(is_match, Solution.re(source, pattern))
