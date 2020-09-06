"""
1. 先翻转各行，把第一列变成1
2. 再翻转除第一列外的其他列，保证1最多。
"""
from typing import List


class Solution:
    @staticmethod
    def matrix_score(a: List[List[int]]) -> int:
        """
        由于行和列都可以翻转
        可以这样看，n*m的每个格子都具有一个权重，其中每一行权重都自左向右递减，
        为使总和最大则尽可能使权重大的格子填"1"。
        """
        n, m = len(a), len(a[0])
        for i in range(n):
            if a[i][0] == 0:
                # 如果当前行的第一个元素为0，尝试翻转当前行(翻转后不一定能让第一个元素为1，但是有必要试试)
                for j in range(m):
                    # 利用异或进行翻转
                    a[i][j] = 1 ^ a[i][j]
        res = 0
        # 逐列逐列地扫描
        for col in zip(*a):
            m -= 1
            # 当前列的权重 * 当前列最多能有几个1
            res += 2 ** m * max(col.count(1), col.count(0))
        return res
