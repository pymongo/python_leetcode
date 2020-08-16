import unittest


class Solution(unittest.TestCase):
    TEST_CASES = [
        # LCS is AC
        ("ABCD", "EACB", 2),
    ]

    def test(self):
        for A, B, lcs in self.TEST_CASES:
            self.assertEqual(lcs, self.f(A, B))

    @staticmethod
    def f(A: str, B: str) -> int:
        m, n = len(A), len(B)
        # 前缀匹配型动态规划: dp[i][j]表示A的前i个字符和B的前j个字符的lcs长度
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # dp[i-1][j]: 不选A[i-1]选B[j-1]
                # dp[i][j-1]: 不选B[j-1]选A[i-1]
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                if A[i - 1] == B[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

        return dp[m][n]
