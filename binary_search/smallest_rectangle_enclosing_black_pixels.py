import unittest
from typing import List


class Solution(unittest.TestCase):
    TEST_CASES = [
        (["0010", "0110", "0100"], 0, 2, 6),
        (["1110", "1100", "0000", "0000"], 0, 1, 6),
    ]

    def test(self):
        for image, x, y, area in self.TEST_CASES:
            self.assertEqual(area, self.f(image, x, y))

    @staticmethod
    def f(image: List[str], x: int, y: int) -> int:
        """
        给你一个黑色点连通的图，还有其中一个黑色点的坐标(x, y)，求出能包含所有黑色点的最小的矩阵体积
        最佳方案: 四次二分，分别去找上下左右的边界，以左右为例，一次二分模板是从0到y的find_first，另一次是从y到n-1的find_last
        实在不会的话，那就BFS也是可以AC的
        """
        m = len(image)
        if m == 0:
            return -1
        n = len(image[0])

        # 分别往左和往右逐列扫，找到矩阵的左边界, 注意扫描列传参size用的是行数m
        # FIXME y的范围虽然是0..n，但是从上往下扫一列的范围size=总行数m
        left = Solution.find_first(image, 0, y, m, Solution.check_column)
        # print("left", left)
        right = Solution.find_last(image, y, n - 1, m, Solution.check_column)
        # print("right", right)

        up = Solution.find_first(image, 0, x, n, Solution.check_row)
        # print("up", up)
        down = Solution.find_last(image, x, m - 1, n, Solution.check_row)
        # print("down", down)

        return (right - left + 1) * (down - up + 1)

    @staticmethod
    def find_first(
        image: List[str],
        start: int,
        end: int,
        size: int,
        check_func: '(List[str], int, int) -> bool'
    ) -> int:
        while start + 1 < end:
            mid = start + (end - start) // 2
            if check_func(image, mid, size):
                end = mid
            else:
                start = mid
        if check_func(image, start, size):
            return start
        return end

    @staticmethod
    def find_last(
        image: List[str],
        start: int,
        end: int,
        size: int,
        check_func: '(List[str], int, int) -> bool'
    ) -> int:
        while start + 1 < end:
            mid = start + (end - start) // 2
            if check_func(image, mid, size):
                start = mid
            else:
                end = mid
        if check_func(image, end, size):
            return end
        return start

    @staticmethod
    def check_column(image: List[str], col: int, m: int) -> bool:
        """
        检测一列有没有黑色的点
        """
        for i in range(m):
            if image[i][col] == '1':
                return True
        return False

    @staticmethod
    def check_row(image: List[int], row: int, n: int) -> bool:
        """
        检测一行有没有黑色的点
        """
        for j in range(n):
            if image[row][j] == '1':
                return True
        return False
