"""
https://leetcode.com/problems/maximum-subarray/
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
O(n)的算法：贪心: if cur_sum+nums[i] < nums[i]，则以舍弃前面的元素，从i开始从新算最大长度
O(n)的算法：动态规划(「滚动数组」): 如果当前元素的前一个元素大于0，则当前元素的值 += 前一个元素的值
O(logn)的算法?分治?: 求区间内最值用「线段树」，但是加上预处理之后，就跟贪心一样是O(n)，本题没有logn的解法
这个分治方法类似于「线段树求解 LCIS 问题」的 pushUp 操作
"""
import unittest
from typing import List, Tuple

MIN_INT = -(2 ** 8)


class Solution:
    @staticmethod
    def brute_force(nums: List[int]) -> int:
        size: int = len(nums)
        max_sum: int = nums[0]
        for i in range(size):
            temp_sum = nums[i]
            for j in range(i + 1, size):
                temp_sum += nums[j]
                if max(temp_sum, nums[j]) > max_sum:
                    max_sum = max(temp_sum, nums[j])
        return max_sum

    @staticmethod
    def dp(nums: List[int]) -> int:
        """
        动态规划-滚动数组
        """
        size = len(nums)
        # assert size >= 1
        max_sum = nums[0]
        for i in range(1, size):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(max_sum, nums[i])
        return max_sum

    @staticmethod
    def greedy(nums: List[int]) -> int:
        size = len(nums)
        # assert size >= 1

        cur_sum = max_sum = nums[0]
        for i in range(1, size):
            # 贪心: 如果for循环的当前数组指针元素 加上 之前元素的和 小于0，则丢弃之前的元素，从当前位置开始从新计算cur_sum
            # 本题的贪心思路有点像Gas Station一题
            cur_sum = max(cur_sum+nums[i], nums[i])
            max_sum = max(max_sum, cur_sum)

        return max_sum


class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[List[int], int]] = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([-1, 0, -2], 0),
        ([-2, 1], 1),
        ([1], 1),
    ]

    def test_brute_force(self):
        for input_array, expected in self.TEST_CASES[:]:
            self.assertEqual(expected, Solution.brute_force(input_array))

    def test_greedy(self):
        for input_array, expected in self.TEST_CASES[:]:
            self.assertEqual(expected, Solution.greedy(input_array))

    def test_dp(self):
        for input_array, expected in self.TEST_CASES[:]:
            self.assertEqual(expected, Solution.dp(input_array))
