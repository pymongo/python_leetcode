import unittest
from typing import List


class Solution:
    """
    输入一个杨辉三角形状的二维数组，从根出发，只能往左下或右下走，求从根到底层的最短路径的长度
    假设层数为n, 除了O(n^2)的DP解,
    还有2^n(相当于所有路径穷举一次，到n层总共2^n条路径)的DFS搜索法,
    类似二叉树的分治法O(2^n)遍历，时间复杂度仍然是2^n，没有剪枝，所有抉择都是一分为二，所以还是跟DFS搜索全部路径一样
    因为分治法没有避免重复计算，没有记忆之前计算的结果，如果用全局HashMap，key为数组坐标, value为最短路径值，能避免重复计算
    记忆化搜索只是动态规划的一种实现方式，用分治法也能实现动态规划
    O(n)时间复杂度的题不适合用记忆化搜索，栈的深度也是O(n)容易Stack Overflow
    常用的动态规划实现方法是递推(for循环迭代填表)，二维数组dp的下标(i,j)表示一个子问题
    动态规划能解决 求最值、问可行性、求方案总数 的问题
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
    def try_dp_one_traverse(triangle: List[List[int]]) -> int:
        size = len(triangle)
        root_val = triangle[0][0]
        if size < 2:
            return root_val
        triangle[1][0] += root_val
        triangle[1][1] += root_val
        # 一次遍历的解法
        for i in range(2, size):
            # 每层的左边界
            triangle[i][0] += triangle[i - 1][0]
            # 每层的右边界
            triangle[i][i] += triangle[i - 1][i - 1]
            # 每层的中间
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[size - 1])

    @staticmethod
    def dp_bottom_to_top(triangle: List[List[int]]) -> int:
        # 眼前一亮的解法: 从自下而上的DP
        # 注意面试题是否允许你修改入参的数组
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

    def test_try_dp_one_traverse(self):
        for triangle, shortest_path in self.TEST_CASES:
            self.assertEqual(shortest_path, Solution.try_dp_one_traverse(triangle))
