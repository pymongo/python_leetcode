import unittest


class Solution:
    """
    原来的爬楼梯是1步或2步(斐波那契数列)，这题是1/2/3步
    f(n)=f(n-1)+f(n2)+f(n-3)
    n: 0 1 2 3 4
    f: 1 1 2 4 7
    """

    @staticmethod
    def solution(n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        p1, p2, p3 = 1, 1, 2
        for _ in range(n - 2):
            p1, p2, p3 = p2, p3, p1 + p2 + p3
        return p3


class Testing(unittest.TestCase):
    def test(self):
        self.assertEqual(7, Solution.solution(4))
