import unittest
import itertools


# 耗时8s的排列组合解法
def check_reordered_power_of_2(n: int) -> bool:
    if n == 0:
        return False
    if (n & -n) == n:
        return True
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    size = len(digits)
    last = size - 1
    # 使用迭代器逐个计算排列组合，避免一次性计算344353235这种大数据会超时
    all_digits = iter(itertools.permutations(digits))
    while True:
        nums = next(all_digits, None)
        if nums is None:
            return False
        if nums[0] == 0:
            continue
        if nums[last] % 2 != 0:
            continue
        num = sum(digit * (10 ** (last - i)) for i, digit in enumerate(nums))
        if (num & -num) == num:
            return True


# 耗费3秒，更优化的排列组合解法
def better_permutation_solution(n: int) -> bool:
    if n == 0:
        return False
    if (n & -n) == n:
        return True
    str_n = str(n)
    all_possibles = iter(itertools.permutations(str_n))
    while True:
        nums = next(all_possibles, None)
        if nums is None:
            return False
        if nums[0] == '0':
            continue
        num = int("".join(nums))
        if (num & -num) == num:
            return True


from collections import Counter


# Java实现Counter类型: 长度为10的数组，索引表示0-9每位，值表示出现次数
# Java可以在static块中初始化2**1到2**31的Counter
# 参考power_of_4的官方解答，可读性更好的做法是定义另外一个数据类去初始化POSSIBLE_VALUES
class Solution:
    # 不用Counter仅比较字符串的最快解答以及数据结构
    # TODO return ''.join(sorted(str(N))) in {''.join(sorted(str(1<<i))) for i in range(30)}
    POSSIBLE_VALUES = [Counter(str(2 ** power)) for power in range(31)]

    # 查询入参范围内的每一个2的幂的每位组成(Counter)，如果Counter(n)等于其中一个，则返回True
    def check_reordered_power_of_2(self, n):
        if n == 0:
            return False
        counter = Counter(str(n))
        for value in self.POSSIBLE_VALUES:
            if counter == value:
                return True
        return False


class Testing(unittest.TestCase):
    TEST_CASE = [
        (1, True),
        (10, False),
        (16, True),
        (24, False),
        (46, True),
    ]

    def test(self):
        for n, expected in self.TEST_CASE:
            self.assertEqual(expected, check_reordered_power_of_2(n))
