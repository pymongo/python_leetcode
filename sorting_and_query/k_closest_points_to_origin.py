"""
求平面坐标下一个点到原点的距离，不需要求平方根，直接比较x^2+y^2即可
本题要求返回前k小的元素(可以理解为排序后取前k项的数组切片)，第k大/小问题可以用quick select
而题目不要求前k项有序，所以用快速选择算法也可以
"""

from typing import List
import unittest
from copy import deepcopy


# Runtime: 668 ms, faster than 91.41% of Python3
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
    return points[:k]

# leetcode没有要求前k项目有序，所以可以使用快速选择算法
# def k_closest_quick_select(points: List[List[int]], k: int) -> List[List[int]]:
#     return []


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


def lintcode_sort_by_multi_keys(points: List[Point], origin: Point, k: int) -> List[Point]:
    # 如果两个点有相同距离，则按照x值来排序；若x值也相同，就再按照y值排序
    points.sort(key=
                lambda point: (
                    (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2,
                    point.x,
                    point.y)
                )
    return points[:k]


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]])
    ]

    def test_k_closest(self):
        for points, k, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, k_closest(points, k))
