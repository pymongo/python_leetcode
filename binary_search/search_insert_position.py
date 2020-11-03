import unittest
from typing import List


# 二分查找target在有序数组中应该插入到哪个下标位置，数组无重复元素
class Solution(unittest.TestCase):
    TESTCASES = [
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
    ]

    def test(self):
        for nums, target, expected in self.TESTCASES:
            self.assertEqual(expected, self.search(nums, target))

    @staticmethod
    def search(nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            # Python右移除要多加一对括号
            # mid = start + ((end - start) >> 1)
            mid = start + end - start // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                # 例如[1,2],2 -> [1,2,2], target的2插入的数组老的2的前面
                return mid
        if nums[start] >= target:
            return start
        else:
            return start + 1
