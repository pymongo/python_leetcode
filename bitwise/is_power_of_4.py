"""
nim_game中的关于4的倍数的位运算规律
先来看一组4的倍数的二进制表示
    4       0100
    8       1000
    12      1100
    16     10000
    20     10100
由此可见 4 的倍数的二进制表示的后 2 为一定为 0
从另外一个角度来看，4 的二进制表示是 0100，任何 4 的倍数一定是在此基础上增加 n 个 0100
所以如果n是4的倍数，那么(n&3)==0
"""

import unittest
import random
import math


def my_bitwise(n: int) -> bool:
    if n == 0:
        return False
    if n == 1:
        return True
    # 4的幂同时也是2的幂
    if (n & -n) != n:
        return False
    # 4的幂的个位只能是4或6
    one_place = n % 10
    if one_place != 4 and one_place != 6:
        return False
    return True
    # return (n & -n) == n and (n & 3) == 0


# 理论根据: 如果一个数是2的幂，那么它的二进制表示中有且只有一位是1
def bitwise_solution_1(n: int) -> bool:
    """
    (n & -n): 只获取n的二进制的从左到右第一个1，其余位置0，如果n的二进制中只有一个1，那么(n & -n) == n
    Example1:
     3 = 0011
    -3 = 1101
    3 & -3 = 1
    Example2:
     4 = 0100
    -4 = 1100
    4 & -4 = 0100
    """
    if n == 0:
        return False
    return (n & -n) == n


def bitwise_solution_2(n: int) -> bool:
    pass


class Testing(unittest.TestCase):
    def test_my_solution(self):
        for _ in range(10 ** 4):
            n = random.randint(0, 10 ** 9)
            expected: bool = math.log(n, 4).is_integer()
            self.assertEqual(expected, my_bitwise(n))
