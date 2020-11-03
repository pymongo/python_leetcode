import unittest
from typing import List


class Solution(unittest.TestCase):
    TESTCASES = [
        ([
             [1, 4, 7, 11, 15],
             [2, 5, 8, 12, 19],
             [3, 6, 9, 16, 22],
             [10, 13, 14, 17, 24],
             [18, 21, 23, 26, 30]
         ], 5, True),
        ([
             [1, 4, 7, 11, 15],
             [2, 5, 8, 12, 19],
             [3, 6, 9, 16, 22],
             [10, 13, 14, 17, 24],
             [18, 21, 23, 26, 30]
         ], 20, False),
    ]

    def test(self):
        for matrix, target, is_in_matrix in self.TESTCASES:
            self.assertEqual(is_in_matrix, self.is_in_matrix(matrix, target))

    @staticmethod
    def is_in_matrix(matrix: List[List[int]], target: int) -> bool:
        """
        给你一个每行每列都有序，但是整体未必有序的数组，判断target是否在数组中
        思路: 从左下角或右上角开始搜索
        选左上角，往右走和往下走都增大，不能选(如果给矩阵横竖切两刀，选左上角就只能排除掉1/4块)
        选右下角，往上走和往左走都减小，不能选
        选左下角，往右走增大，往上走减小，可选(一次排除一行或一列)
        选右上角，往下走增大，往左走减小，可选
        这题的算法实际上「不是二分法」
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            num = matrix[row][col]
            if num > target:
                col -= 1
            elif num < target:
                row += 1
            else:
                return True
        return False

    @staticmethod
    def count_target_in_matrix_lintcode(matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        row, col = 0, n - 1
        cnt = 0
        while row < m and col >= 0:
            num = matrix[row][col]
            if num > target:
                # 排除掉一列
                col -= 1
            elif num < target:
                # 排除掉一行
                row += 1
            else:
                # lintcode上每行和每列没有重复元素，所以如果发现等于target就可以同时排除掉一行和一列
                cnt += 1
                row += 1
                col -= 1
        return cnt
