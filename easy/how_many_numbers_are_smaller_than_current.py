import unittest
from typing import List


# 这题除了暴力两遍循环，不太适合用排序，排序记住排序前索引不算难，难点在于数个数时如何去重
# 由于题目限定数字范围是0..=100，所以推荐使用前缀和(也就是cnt[i]=nums[0]+nums[1]+...+nums[i])
# 前缀和的典型应用就是股票OrderBook的深度列(例如从卖单的最低价一直累加到当前价格的股票数量)
class Solution(unittest.TestCase):
    TEST_CASES = [
        ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
        ([5, 0, 10, 0, 10, 6], [2, 0, 4, 0, 4, 3])
    ]

    def test(self):
        for nums, output in self.TEST_CASES:
            self.assertEqual(output, self.f(nums))

    @staticmethod
    def f(nums: List[int]) -> List[int]:
        cnt = [0] * 101

        # count num in nums
        for num in nums:
            cnt[num] += 1
        # calc cumulative prefix sum
        for i in range(1, 101):
            cnt[i] += cnt[i - 1]

        output = []
        for i, num in enumerate(nums):
            if num == 0:
                output.append(0)
            else:
                output.append(cnt[num - 1])
        return output
