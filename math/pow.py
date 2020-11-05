"""
https://leetcode.com/problems/powx-n/
快速幂运算:
Example 5**3=?
指数部分3的二进制是11
所以result=5**1+5**2
"""
import random
import unittest


# 假设幂的基数x>0
def my_pow(x: float, n: int) -> float:
    if n == 0:
        return 1
    is_negative = n < 0
    if is_negative:
        n = -n

    result = 1
    base = x
    while n != 0:
        # 幂运算结果等于指数的二进制为1的位 的加权乘积
        # 例如 5**3 = 5**1 * 5**2
        if n % 2 == 1:
            result *= base
        base *= base
        n //= 2
    if is_negative:
        return 1 / result
    else:
        return result


# https://lintcode.com/problem/fast-power/
# Calculate the a**n % b
# 除了快速幂运算，辗转相除法也是一个非二分法的logn算法
# 负数MOD问题: Python/Ruby: -1%3 = 2, Java/Rust: -1%3 = -1
def fast_pow(a: int, b: int, n: int) -> int:
    # if n == 0:
    #     return a % b
    result = 1
    base = a
    while n != 0:
        # 幂运算结果等于指数的二进制为1的位 的加权乘积, 例如 2^5中指数是5，二进制是101，所以2^5=2^4*2^1，只有指数中
        if n % 2 == 1:
            # 随时可以 % b 避免 overflow 其不影响结果，这是 % 运算的特性
            # 四则运算只有除法不满足 % 运算的特性
            result = (result * base) % b
        base = (base * base) % b
        n //= 2
    return result % b


class Testing(unittest.TestCase):
    def test_my_pow(self):
        base = random.uniform(1, 10)
        power = random.randint(-10, 10)
        # print(base, power)
        # self.assertEqual(base ** power, my_pow(base, power))
        self.assertLessEqual(abs(base ** power - my_pow(base, power)), 1e-3)
