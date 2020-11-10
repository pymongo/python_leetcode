import unittest
from heapq import heappush, heappop


def heap_nth_ugly(n: int):
    heap = [(1, 1)]
    # 不断更新堆，每遍历一次就pop掉一个最小值，pop到第N个时就是想要的答案，此时堆的元素个数至少还有n个(冗余部分)
    for _ in range(1, n):
        num, num_factor = heappop(heap)
        for factor in (2, 3, 5):
            # 堆里只接受质因子升序相乘的数
            # 例如2x3能入堆，但是3x2不能
            # 实现上，因为质因子是升序排列，只要记住最后一个质因子就可以了(有点像「单调栈」)
            if factor >= num_factor:
                heappush(heap, (factor * num, factor))
    return heappop(heap)[0]


# 返回ugly_numbers序列中的第N个
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...
def dp_solution(n: int) -> int:
    """
    动态规划的状态转移方程 dp[next] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
    """
    ugly_numbers = [1]
    p2, p3, p5 = 0, 0, 0
    for _ in range(1, n):
        mul_2, mul_3, mul_5 = ugly_numbers[p2] * 2, ugly_numbers[p3] * 3, ugly_numbers[p5] * 5
        min_mul = min(mul_2, mul_3, mul_5)
        ugly_numbers.append(min_mul)
        # 不能用if..elif，否则无法去重2x3=3x2的情况
        if min_mul == mul_2:
            p2 += 1
        if min_mul == mul_3:
            p3 += 1
        if min_mul == mul_5:
            p5 += 1
    return ugly_numbers[n - 1]


class Testing(unittest.TestCase):
    TEST_CASES = [
        (10, 12), (1, 1), (9, 10)
    ]

    def test_factor_solution(self):
        for n, expected in self.TEST_CASES:
            self.assertEqual(expected, dp_solution(n))

    def test_heap_nth_ugly(self):
        for n, expected in self.TEST_CASES:
            self.assertEqual(expected, heap_nth_ugly(n))
