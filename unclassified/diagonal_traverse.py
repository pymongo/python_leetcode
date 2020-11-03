import unittest
from typing import List


class Solution(unittest.TestCase):
    """
    首先有明确需要遍历几次，由于每次遍历都会经过一次「第一行+最后一列」
    所以总共遍历次数等于`↴`的长度，也就是m+n-1
    """
    TESTCASES = [
        ([
             [2, 5, 8],
             [4, 0, -1]
         ], [2, 5, 4, 0, 8, -1]),
        ([
             [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]
         ], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
        ([[2, 3]], [2, 3]),
    ]

    def test(self):
        for matrix, output in self.TESTCASES:
            self.assertListEqual(output, self.f(matrix))

    @staticmethod
    def f(matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        if m == 1:
            return matrix[0]
        n = len(matrix[0])

        res = []
        row, col = 0, 0
        for k in range(m + n - 1):
            if k % 2 == 0:
                # 左下↗右上的↗️对角线方向(x-1,y+1)
                res.append(matrix[row][col])
                while row - 1 >= 0 and col + 1 < n:
                    row, col = row - 1, col + 1
                    res.append(matrix[row][col])

                # 移动到换方向后的起始位置
                if col + 1 < n:
                    col += 1
                else:
                    row += 1
            else:
                # 右上↙左下的↙️对角线方向(x+1,y-1)
                res.append(matrix[row][col])
                while col - 1 >= 0 and row + 1 < m:
                    row, col = row + 1, col - 1
                    res.append(matrix[row][col])

                # 移动到换方向后的起始位置
                if row + 1 < m:
                    row += 1
                else:
                    col += 1
        return res
