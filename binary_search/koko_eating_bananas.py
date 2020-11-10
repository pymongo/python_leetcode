import unittest
from typing import List
import math


class Solution(unittest.TestCase):
    TEST_CASES = [
        ([3, 6, 7, 11], 8, 4),
        ([30,11,23,4,20], 5, 30),
        ([30,11,23,4,20], 6, 23),
    ]

    def test(self):
        for nums, time, min_speed in self.TEST_CASES:
            self.assertEqual(min_speed, self.min_speed(nums, time))

    @staticmethod
    def min_speed(nums: List[int], time: int) -> int:
        # 答案集的二分类型题，类似copy_books和woods_cut
        max_time_cost = max(nums)

        def calc_time_by_speed(speed: int) -> int:
            total_time_cost = 0
            for num in nums:
                total_time_cost += math.ceil(num / speed)
            return total_time_cost

        # left/right表示速度, 二分法find_fisrt模板找到能在k小时干完活的最小的速度
        # 因为1小时至多做一个任务，所以速度的上限是max(nums)
        start, end = 1, max_time_cost
        while start + 1 < end:
            mid = start + (end - start) // 2
            time_cost = calc_time_by_speed(mid)
            if time_cost <= time:
                end = mid
            else:
                start = mid
        if calc_time_by_speed(start) <= time:
            return start
        return end
