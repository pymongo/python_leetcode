import unittest


# 能否找到和为n的一组正整数，使得他们的乘积最大
# 例如 3+3+4=10，和为10的数组中最大乘积是36
class Solution(unittest.TestCase):
    TESTCASES = [
        (2, 1),
        (10, 36)
    ]

    def test_integer_break(self):
        for n, product in self.TESTCASES:
            self.assertEqual(product, self.integer_break(n))

    @staticmethod
    def integer_break(n: int):
        dp = [0] * (n + 1)
        # 只有当整数大于2时才能找到划分点j
        for i in range(2, n + 1):
            for j in range(i):
                # 将i拆分成j和i-j的和，且i-j不再拆分成多个正整数，此时的乘积是jx(i-j)
                # 将i拆分成j和i-j的和，且i-j继续拆分成多个正整数，此时的乘积是jxdp[i-j]
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]
