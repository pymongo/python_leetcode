import unittest
from typing import List


class Solution:
    """
    输入一个杨辉三角形状的二维数组，从根出发，只能往左下或右下走，求从根到底层的最短路径的长度
    """

    # noinspection PyMethodMayBeStatic,PyPep8Naming
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 最底层的元素个数正好也是i
        size = len(triangle)
        # 用滚动数组的感觉不断往下滚，当前节点的最短路径等于上一层连向该节点的两个节点的最小值
        # 例如: 第三层4的最小路径长度是上一层3和4的最短路径长度+4(动态规划)，直接在原数组上改，不需要额外的DP数组
        #  3 4
        # 6 4 7

        # 1. 初始化DP数组中三角形的左边和右边，初始化边界这种特殊情况之后才能正确填表
        for i in range(1, size):
            # 每层的左边界
            triangle[i][0] += triangle[i - 1][0]
            # 每层的右边界
            triangle[i][i] += triangle[i - 1][i - 1]

        # 2. 开始填DP的表
        for i in range(2, size):
            # 不包含每层的左右边界
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        # print(triangle)
        return min(triangle[size - 1])

    @staticmethod
    def dp_bottom_to_top(triangle: List[List[int]]) -> int:
        # 别人的解法: 从自下而上的DP
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] = triangle[i][j] + min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([
             [2],
             [3, 4],
             [6, 5, 7],
             [4, 1, 8, 3]
         ], 11),
        (
            [
                [2],
                [3, 2],
                [6, 5, 7],
                [4, 4, 8, 1]
            ], 12
        )
    ]

    def test(self):
        solution = Solution()
        for triangle, shortest_path in self.TEST_CASES:
            self.assertEqual(shortest_path, solution.minimumTotal(triangle))
