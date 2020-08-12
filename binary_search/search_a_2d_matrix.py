import unittest
from typing import List


class Solution(unittest.TestCase):
    TEST_CASES = [
        ([
             [1, 3, 5, 7],
             [10, 11, 16, 20],
             [23, 30, 34, 50]
         ], 3, True),
        ([
             [1, 3, 5, 7],
             [10, 11, 16, 20],
             [23, 30, 34, 50]
         ], 13, False),
    ]

    def test(self):
        for matrix, target, is_in_matrix in self.TEST_CASES:
            self.assertEqual(is_in_matrix, self.is_in_matrix(matrix, target))

    @staticmethod
    def is_in_matrix(matrix: List[List[int]], target: int) -> bool:
        """
        给你一个排好序的矩阵，判断target是否在矩阵内
        可以先用二分法找到在第几行，再用二分法找到在第几列
        但是这样太慢了，正确做法是矩阵看做一个一维数组(从上到下从左到右的编号)去二分，然后再将一维数组索引值通过除法和取模得到矩阵的x,y
        例如4x4的矩阵，第0个元素的行号是0//4, 列号是0%4
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = start + (end - start) // 2
            i = mid // n
            j = mid % n
            num = matrix[i][j]
            if num > target:
                end = mid - 1
            elif num < target:
                start = mid + 1
            else:
                return True
        return False
