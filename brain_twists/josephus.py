"""
约瑟夫环——圆圈报数出列问题
m=5, m=3时
Round 1:
0 1 2 3 4
    ^
下一轮将从数字3开始
Round 2:
3 4 0 1
    ^
Round 3:
1 3 4
    ^
Round 4:
1 3
^
所以得到重要规律: 最后活下来的数字在最后一轮中的下标为0
通过最后一轮活下来的数字下标0，倒推上一轮中该数字的下标，再倒推上上轮的下标...
一直倒推到第一轮时数字的下标，再次原数组中查询得知最后活下来的数是多少
"""
import unittest


class Solution(unittest.TestCase):
    TEST_CASES = [
        (3, 5, 3),
        (17, 10, 2),
    ]

    def test(self):
        for m, n, expected in self.TEST_CASES:
            self.assertEqual(expected, self.f(m, n))

    @staticmethod
    def f(m: int, n: int) -> int:
        # 最后活下来的数的下标
        idx = 0
        # nums_len表示当前轮一共有几个数字，由于最后一轮有2个数，所以从2开始倒推到元素个数为n的那一轮
        for nums_len in range(2, n+1):
            # 因为剔除数时，所有活下来的是都会循环左移m次，例如[0,1,2,3,4]->[3,4,0,1]，3的下标从3左移到0
            # 那么倒推时，我们需要把idx循环右移
            idx = (idx + m) % nums_len
        return idx
