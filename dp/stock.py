"""
# 状态表示
先记住状态表示: dp[i][k][0/1]表示3种状态下取得的交易最大收益
i表示第几天，也就是prices数组的下标
k表示最多可进行几次交易，一次买+一次卖才算一次交易(transactions)
这里定义为购买股票时k+1，当然也可以让出售股票时k+1
0/1表示是否持有股票，TODO 持有股票的数量是多少?因为本题就只有一股，数量肯定是1股，至于价格就未必是昨天的价格
0/1之间状态转移的选择操作有: buy,sell,rest(无操作)
例如 dp[3][2][1]表示今天是第3个交易日，我还剩两次交易机会，手里持有一些股票

# 状态转移
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
解释: 我今天没有股票，有两种可能
1. 我昨天也没有股票，今天选择rest操作
2. 我昨天持有了股票，今天选择sell操作

dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
解释: 我今天持有股票，有两种可能
1. 我昨天持有了股票，今天选择rest操作
2. 我昨天没有买股票，股票是今天刚买的

# 初始条件
k=0时，不允许交易，收益为-inf
i=0时，收益为0
"""
import unittest
from typing import List
import sys


class Solution(unittest.TestCase):
    @staticmethod
    def stock_1(prices: List[int]) -> int:
        # 最大交易次数为1
        min_price = sys.maxsize
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

    def test_stock_1_dp(self):
        test_cases = [
            ([7, 1, 5, 3, 6, 4], 5)
        ]
        for prices, max_profit in test_cases:
            self.assertEqual(max_profit, self.stock_1_dp(prices))

    @staticmethod
    def stock_1_dp(prices: List[int]) -> int:
        # 第一题k=1，其实可以把k忽略掉
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        # 第一天选择购买股票，支出-prices[0]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            # 第i个交易日没有股票
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 第i个交易日持有股票，因为这题dp[i-1][0]全为0，所以购买股票的值可以简写为-prices[i]
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        # 就看最后一天不持有股票的状态(如果持有了股票那肯定是亏的啊)
        return dp[n - 1][0]

    @staticmethod
    def stock_2(prices: List[int]) -> int:
        # 不限交易次数，只要找到一对递增的价格就累加到收益中
        n = len(prices)
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

