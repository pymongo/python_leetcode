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


# 另一种解法: return num > 0 and log2(num) % 2 == 0
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
    # 不需要判断能否被4整除
    # return (n & -n) == n and (n & 3) == 0


def bitwise_solution_2(n: int) -> bool:
    """
    4=0100的幂只可能在奇数位上有1
    如果n是2的幂同时只有奇数位上是1(n & 0xaaaaaaaa == 0)，那么n是4的幂
    """
    return n > 0 and (n & -n) == n and n & 0xaaaaaaaa == 0


def bitwise_solution_3(n: int) -> bool:
    """
    若 xx 为 2 的幂且 x%3 == 1，则 xx 为 4 的幂
    证明方法: 4^k % 3 = (3+1)^k % 3 = ...(二项式展开) = 1
    """
    return 0 < n == (n & -n) and n % 3 == 1


class Testing(unittest.TestCase):
    def test_my_solution(self):
        for _ in range(10 ** 4):
            n = random.randint(0, 10 ** 9)
            expected: bool = math.log(n, 4).is_integer()
            self.assertEqual(expected, my_bitwise(n))
