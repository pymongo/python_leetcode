"""
分解质因数算法:
枚举质因子 i 从最小的质数2开始到取整sqrt(num)，因为比根号n还要大的因数容易成小数
依次判断 i 是否为 num 的因数
如果是那么存下 i 并且 num/=i ，继续判断
"""

import unittest
from typing import List


# TODO 质因数分解有一种更快的算法，叫做Pollard Rho快速因数分解
# 根号n的算法: 分解质因数、分块检索法(drop_eggs_1)
def my_solution(n: int) -> List[int]:
    # 向上取整
    upper_limit = int(n ** 0.5 + 1)
    result = []
    for k in range(2, upper_limit):
        while n % k == 0:
            result.append(k)
            n //= k
    # 如果最后还有剩余，则为最后一个质因数，例如10的第二个质因数5
    if n != 1:
        result.append(n)
    return result


class Testing(unittest.TestCase):
    TEST_CASES = [
        (660, [2, 2, 3, 5, 11]),
        (10, [2, 5]),
    ]

    def test(self):
        for n, prime_factors in self.TEST_CASES:
            self.assertEqual(prime_factors, my_solution(n))
