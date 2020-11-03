""" https://leetcode.com/problem/regular-expression-matching/
这题跟wildcard_matching不同的是，星号的含义不同
c*表示可以匹配任意个c
".*" 表示可匹配零个或多个（'*'）任意字符（'.'）
ab可以被".*"匹配

这题最快解法应该是「有限状态机/自动机」
"""
import unittest


class Solution(unittest.TestCase):
    TESTCASES = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
    ]

    def test_re(self):
        for source, pattern, is_match in self.TESTCASES:
            print(source, pattern)
            self.assertEqual(is_match, Solution.re(source, pattern))

    @staticmethod
    def re(s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 空的source字符串可以被空的pattern匹配上
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # 首先 * 是不会在 p[0] 的，它之前必须有个字符，所以在匹配 p[j - 1] == '*' 能进入 if 代码块儿时，j 至少为 2
                    # 所以j-2不会越界
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        # dp[i][j-2]  : a* counts as empty
                        # dp[i-1][j-2]: a* counts as single a
                        # dp[i-1][j]  : a* counts as multiple a
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
                    else:
                        # 由于s[i]和s[j]不一样，所以只有*不选的情况, dp[i][j-1]表示*不选的情况, 与wildcard不同的是，星号不选则表示星号前面的字母也不选
                        dp[i][j] = dp[i][j - 2]
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]
