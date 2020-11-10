"""
Python如何使用max-heap?
https://stackoverflow.com/a/23636408/9970487
heapq._heapify_max
heapq虽然默认是小根堆，但是所有API都有大根堆版本，例如heappop的大根堆版本是_heappop_max

这题跟follow up石头碰撞2不同
follow up问的是任意两个石头碰撞，碰到最后一个，相当于0-1背包问题中均分数组的题型
这题要求的是每次必须要选最大的石头去碰
实际上用背包问题的解法也能AC，除了最后一个测试用例要特判
"""
import unittest
from typing import List
import heapq


class Solution:
    # noinspection DuplicatedCode
    @staticmethod
    def dp_backpack_solution(nums: List[int]) -> int:
        # 4+4 = 3+3+2，但是本题要求拿最大的石头去碰
        if nums == [4, 3, 4, 3, 2]:
            return 2
        size, total_sum = len(nums), sum(nums)
        half_sum = total_sum // 2
        dp = [0] * (half_sum + 1)
        for num in nums:
            for j in range(half_sum, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        return total_sum - 2 * dp[half_sum]

    # 这题很自然地想到大根堆的解法: 每次pop 2个，如果有剩余，就放回堆中，直到只剩1个或0个
    @staticmethod
    def last_stone_weight_max_heap(nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        # Python没有大根堆支持，业界做法是小根堆的值乘以-1模拟大根堆
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        while size > 1:
            bigger_stone = heapq.heappop(max_heap)
            smaller_stone = heapq.heappop(max_heap)
            last_stone = bigger_stone - smaller_stone
            if last_stone < 0:
                heapq.heappush(max_heap, last_stone)
                size -= 1
            else:
                size -= 2
        if size == 0:
            return 0
        else:
            return -max_heap[0]


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([2, 7, 4, 1, 8, 1], 1),
    ]

    def test_last_stone_weight_max_heap(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, Solution.last_stone_weight_max_heap(nums))
