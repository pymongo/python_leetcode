"""
给定一个正整数n，找到最小的正整数b，使得b的从左到右每位数字相乘结果等于n
"""
import unittest


def solution(n: int) -> int:
    res = ''
    # 贪心算法: 由于是每位数字的乘积，所以因数范围只可能是[2,9]，为了让b尽可能小，所以要让较大的因数9尽可能排在个位，所以要先除以9
    # 一定要让较大的因数先被除，避免48被分解成22223
    for k in range(9, 1, -1):
        while n % k == 0:
            # 注意结果是先塞入较大因数，所以后面要逆序
            # 或者写成 res = str(k) + res 的方式逆序插入
            res += str(k)
            n //= k
    # n是质数的情况
    if n != 1:
        return 0
    res_int = int(res[::-1])
    if res_int > 0x7fffffff:
        return 0
    else:
        return res_int


class Testing(unittest.TestCase):
    TESTCASES = [
        (48, 68),
        (15, 35)
    ]

    def test(self):
        for n, expected in self.TESTCASES:
            self.assertEqual(expected, solution(n))
