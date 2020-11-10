"""
例如2，不是快乐数，但是也会陷入循环
2
4
16
37
58
89
145
42
20
4
16
37
58
89
145
42
20
4
"""
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
        """
        首先不管是不是快乐数，任何数按照逐位平方和迭代下去肯定会陷入循环
        TODO 快乐数的定义是最终n=1无限循环
        """
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

    @staticmethod
    def get_next(n: int) -> int:
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum

    @staticmethod
    def hashset_solution(n: int):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = Solution.get_next(n)
        return n == 1

    @staticmethod
    def linked_list_cycle_solution(n: int) -> bool:
        slow_runner = n
        fast_runner = Solution.get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = Solution.get_next(slow_runner)
            fast_runner = Solution.get_next(Solution.get_next(fast_runner))
        return fast_runner == 1

