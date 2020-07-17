"""
    1 0b1
    3 0b11
    9 0b1001
   27 0b11011
   81 0b1010001
  243 0b11110011
  729 0b1011011001
3的幂的规律(自己瞎猜的)
1. 个位是1,3,9,7: n%3=0 or 1
2. 二进制最后一位是1: (n & -n) == 1
3. 二进制最高位是1: ?

获取从右边往左第一位非0 bit的索引位置的方法: math.log2(n&-n)+1
"""

import unittest
import random
import math


# 另一种解法: return num > 0 and log2(num) % 2 == 0
def my_bitwise(n: int) -> bool:
    if n < 0:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    # 二进制最后一位是1
    if (n & -n) != 1:
        return False
    while n > 3:
        if n % 3 != 0:
            return False
        n //= 3
    return True


class Testing(unittest.TestCase):
    # 找规律用
    def test_print_power_of_3(self):
        for n in range(10):
            num = 3 ** n
            print('%5s' % num, bin(num))
            # 1
            print(num & -num)
            print(num % 3)

    def test_my_solution(self):
        self.assertEqual(True, my_bitwise(27))
        for _ in range(500):
            n = random.randint(0, 10 ** 9)
            print(n)
            expected: bool = math.log(n, 3).is_integer()
            self.assertEqual(expected, my_bitwise(n))
