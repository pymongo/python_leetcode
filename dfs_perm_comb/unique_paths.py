import math


class Solution:
    """
    棋盘大小是mxn，可以理解成有每行有m个端点，但是只有m-1个线段

    如何抽象成组合数问题?

    由于只能向下或向右走，等同于从总共从m-1+n-1个线段中选n-1的线段向右走
    """

    @staticmethod
    def comb_solution(m: int, n: int) -> int:
        return math.comb(m - 1 + n - 1, n - 1) if m > n else math.comb(n - 1 + m - 1, m - 1)
