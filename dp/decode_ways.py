import unittest

two_digits = {'10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'}


class Solution(unittest.TestCase):
    TESTCASES = [
        ("301", 0),
        ("100", 0),
        ("10", 1),
        ("226", 3),
        # "1"+"2" or "12"
        ("12", 2),
    ]

    def test(self):
        for s, expected in self.TESTCASES:
            print(s)
            self.assertEqual(expected, self.f(s))

    @staticmethod
    def f(s: str) -> int:
        def decode(_s: str) -> int:
            # 巧妙在于如果不在编码表里返回0，0*dp[any]=0，返回值当作dp的系数去看待
            size = len(_s)
            code = int(_s)
            if size == 1 and 1 <= code <= 9:
                return 1
            if size == 2 and 10 <= code <= 26:
                return 1
            return 0

        # non-empty string containing only digits
        n = len(s)
        if n == 0:
            return 0
        first = decode(s[0])
        # 第0项一开始是dummy的，例如"12"实际上取的是dp[2]，而初始化时dp=[2,2,0]
        dp = [first, first, 0]

        if dp[0] == 0:
            return 0

        if n == 1:
            return dp[0]

        for i in range(2, n + 1):
            dp[i % 3] = dp[(i - 1) % 3] * decode(s[i - 1:i]) \
                        + dp[(i - 2) % 3] * decode(s[i - 2:i])
        return dp[n % 3]
