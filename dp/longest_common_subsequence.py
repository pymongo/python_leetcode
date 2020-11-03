import unittest


class Solution(unittest.TestCase):
    TESTCASES = [
        # LCS is AC
        ("ABCD", "EACB", 2),
    ]

    def test(self):
        for A, B, lcs in self.TESTCASES:
            self.assertEqual(lcs, self.f(A, B))

    @staticmethod
    def f(A: str, B: str) -> int:
        # 这题不太容易也没必要将状态压缩成一维
        m, n = len(A), len(B)
        # 前缀匹配型动态规划: dp[i][j]表示A的前i个字符和B的前j个字符的lcs长度
        # 一行的DP解法是从右往左填表
        dp = [[0] * (n + 1) for _ in range(2)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # TODO 没有A[i-1]和B[j-1]都不选的情况，两个都不选就是dp[i-1][j-1]，所以dp[i-1][j-1]至少要选一个
                if A[i - 1] == B[j - 1]:
                    # A[i-1]和B[j-1]都选上!
                    dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - 1] + 1)
                else:
                    # dp[i-1][j]: 不选A[i-1]选B[j-1]
                    # dp[i][j-1]: 不选B[j-1]选A[i-1]
                    dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])
        return dp[m % 2][n]
