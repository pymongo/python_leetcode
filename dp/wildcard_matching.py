import unittest

# 这题最快解法应该是「有限状态机/自动机」
class Solution:
    @staticmethod
    def wildcard_matching(s: str, p: str) -> bool:
        """
        @param s:
        @param p: pattern
        先抄题解，不懂就背，再不懂就默写
        """
        m, n = len(s), len(p)

        # dp[i][j]表示s的前i个字符能否匹配上pattern的前j个字符
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 初始条件: 2. 空pattern不能匹配任何字符串 dp[..][0]=False
        # 初始条件: 3. 空source字符串仅有星号才能匹配上 dp[0][j]=False
        dp[0][0] = True

        for j in range(1, n + 1):
            # 注意p[j-1]是第j个字符
            if p[j - 1] == '*':
                # pattern的前i个字符串全是*才能匹配上
                dp[0][j] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # 主要从不使用星号(dp[i][j - 1])和使用星号(dp[i-1][j])分开讨论
                    # 1. 如果第j个字符是星号
                    # 1.1 (dp[i][j-1]=>dp[i][j])如果星号匹配的是空字符串，而且dp[i][j-1]能匹配上，那么dp[i][j]也能匹配上
                    # 1.2.1 (dp[i-1][j-1]=>dp[i][j])如果星号匹配的是第i个字符s[i-1]，而且dp[i-1][j-1]能匹配上，那么dp[i][j]也能匹配上
                    # 1.2.2 如果星号匹配了两个字母(第i-1到第i个字符)，dp[i][j]还等于 dp[i-1][j-1] or dp[i-2][j-1]
                    # 1.2.* dp[i][j]等于一堆东西(星号匹配0..=i个字符)或起来: dp[i-1..0][j-1]
                    # 1.2.* 由于后面这些状态是从i-1开始往后的，而且从小遍历到大时，前面的都已经访问过，所以只需要考虑dp[i-1][j]就行了
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[i - 1]:
                    # 2.1 如果p[j]是问号，那么s[i]是任意一个字符即可
                    # 2.2 如果p[j]是小写字母，那么s[i]必须也为相同的小写字母
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


class Testing(unittest.TestCase):
    TESTCASES = [

    ]

    def test(self):
        pass
