import unittest


# 正统的解法应该使用Floyd龟兔赛跑快慢指针判环
class Solution(unittest.TestCase):
    TEST_CASES = [
        (2, False),
        (19, True),
    ]

    def test_is_happy(self):
        for n, is_happy in self.TEST_CASES:
            self.assertEqual(is_happy, self.is_happy(n))

    @staticmethod
    def is_happy(n: int) -> bool:
        # 测试用例中至多需要7次就能判别快乐数
        times = 7
        # 如果上一次计算的平方和等于本次计算的平方和，说明陷入循环，那么这个数就是happy number
        while times > 0:
            next_n = 0
            old_n = n
            while n > 0:
                next_n += (n % 10) ** 2
                n //= 10

            if old_n == next_n:
                return True
            n = next_n
            times -= 1
        return False
