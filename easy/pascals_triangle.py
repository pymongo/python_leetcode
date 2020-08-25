import math
from typing import List


class Solution:
    @staticmethod
    def pascals_triangle_1(n: int) -> List[List[int]]:
        return [[math.comb(row, i) for i in range(row + 1)] for row in range(n)]

    @staticmethod
    def pascals_triangle_2(n: int) -> List[int]:
        return [math.comb(n, i) for i in range(n + 1)]
