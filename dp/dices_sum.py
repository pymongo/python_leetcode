from typing import List


class Solution:
    @staticmethod
    def solution(n: int) -> List[float]:
        # dp[i][j] 表示扔完i个骰子后，点数j的出现次数
        dp = [[0] * (6 * n + 1) for _ in range(n + 1)]
        for i in range(1, 7):
            dp[1][i] = 1
        for i in range(2, n + 1):
            # 第二个骰子，点数至少是2
            for j in range(i, 6 * i + 1):
                for point in range(1, 7):
                    if j - point < 0:
                        break
                    # 例如第二个骰子，12只可能是6+6，但是11可以是6+5或5+6，所以要累加
                    dp[i][j] += dp[i - 1][j - point]
        states_count = 6 ** n
        res = []
        for i in range(n, 6 * n + 1):
            res.append(round(dp[n][i] / states_count, 5))
        return res
