import unittest
from typing import List


class Solution(unittest.TestCase):
    TEST_CASES = [
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
        for matrix, target, is_in_matrix in self.TEST_CASES:
            self.assertEqual(is_in_matrix, self.is_in_matrix(matrix, target))

    @staticmethod
    def is_in_matrix(matrix: List[List[int]], target: int) -> bool:
        """
        给你一个每行每列都有序，但是整体未必有序的数组，判断target是否在数组中
        思路: 从左下角或右上角开始搜索
        选左上角，往右走和往下走都增大，不能选
        选右下角，往上走和往左走都减小，不能选
        选左下角，往右走增大，往上走减小，可选
        选右上角，往下走增大，往左走减小，可选
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
