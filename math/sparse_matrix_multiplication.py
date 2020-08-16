import unittest
from typing import List


# 线性代数之矩阵乘法: A的第一行乘以B的第一列等于结果的第一行第一个，A[0]*B的第二列等于结果的第一行的第二个
# 所谓稀疏矩阵指的是矩阵大部分为0，只有几个数不是0
# FIXME 如果面试官问优化方案，可以答GPU运算，GPU有对矩阵运算的硬件加速，而CPU只能逐行逐列的扫
# noinspection PyPep8Naming
class Solution(unittest.TestCase):
    TEST_CASES = [
        ([[1, 0, 0],
          [-1, 0, 3]],
         [[7, 0, 0],
          [0, 0, 0],
          [0, 0, 1]],
         [[7, 0, 0],
          [-7, 0, 3]])
    ]

    def test(self):
        for A, B, expected in self.TEST_CASES:
            self.assertEqual(expected, self.brute_force(A, B))

    @staticmethod
    def brute_force(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # 题目说明了A的列数等于B的行数
        # 令A的大小为m*n, B的大小为n*l, 则输出矩阵的大小为m*l
        m = len(A)
        n = len(A[0])
        l = len(B[0])
        res = [[0] * l for _ in range(m)]

        # 避免重复计算，下面是错的，要求的是两两逐个相乘后相加
        # a_rows_sum = []
        # for i in range(m):
        #     a_rows_sum.append(sum(A[i]))
        # b_cols_sum = []
        # for i in range(n):
        #     col_sum = 0
        #     for j in range(l):
        #         col_sum += B[i][j]
        #     b_cols_sum.append(col_sum)
        # print(a_rows_sum)
        # print(b_cols_sum)

        # O(n^3)的时间复杂度
        for i in range(m):
            for j in range(l):
                # 一种贪心的优化思路(只适合本题):
                # 另一种思路是预处理只挑出非0的，避免重复计算
                if A[i][j] == 0:
                    continue
                for k in range(n):
                    # i,j=0,0时，表示A的第一行A[0][k]逐个乘B的第一列[k][0]
                    res[i][j] += A[i][k] * B[k][j]

        return res
