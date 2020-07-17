import unittest
import random
import math


# 判断一个整数是否是2的幂
def my_solution(n: int) -> bool:
    if n == 0:
        return False
    if n == 1:
        return True
    # 除了1, power of 2的个位只可能是2,4,6,8
    if n % 2 != 0:
        return False
    n //= 2
    while n != 0:
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        n //= 2
    return True


# dichotomy二分法
def best_dichotomy(n: int) -> bool:
    if n == 0:
        return False
    while n % 2 == 0:
        n /= 2
    return n == 1


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
    """
    (n - 1) 代表了将 n 最右边的 1 设置为 0，并且将较低位设置为 1
    (n & n-1): 去掉n的二进制中最后一个1，如果去掉之后等于0则说明是2的幂
    Example1:
    3 = 0011
    2 = 0010
    3 & 2 = 1
    Example2:
    4 = 0100
    3 = 0011
    4 & 3 = 0
    """
    if n == 0:
        return False
    return (n & n-1) == 0


class Testing(unittest.TestCase):
    def test_my_solution(self):
        for _ in range(10 ** 3):
            n = random.randint(0, 10 ** 6)
            expected: bool = math.log2(n).is_integer()
            self.assertEqual(expected, my_solution(n))
