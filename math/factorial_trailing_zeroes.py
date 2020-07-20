import unittest


# 统计n的阶乘末尾总共有几个0
def solution(n: int) -> int:
    zeroes_count = 0
    while n != 0:
        n //= 5
        zeroes_count += n
    return zeroes_count


class Testing(unittest.TestCase):
    TEST_CASES = [
        (3, 0),
        (5, 1)
    ]

    def test(self):
        for n, factorial_trailing_zeroes_count in self.TEST_CASES:
            self.assertEqual(factorial_trailing_zeroes_count, solution(n))
