"""
https://leetcode.com/problems/3sum/
判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组
不重复意味着[1,1,0,-1]中只有一组解，用第一个1和第二个1组成的解视为一个
模式识别: 利用排序避免重复的解
"""

import unittest
from typing import List


def three_sum_equal_zero(nums: List[int]) -> List[List[int]]:
    result = []
    # 通过shadowing重新赋值的好处是排序时不会修改掉原来的nums数组
    nums = sorted(nums)
    length = len(nums)
    last_index = length - 1
    for i in range(length):
        # 从小到大搜索，跳过重复值
        if i > 0 and nums[i] == nums[i-1]:
            continue
        right = last_index
        target = -nums[i]
        for left in range(i+1, length):
            if left > i+1 and nums[left] == nums[left-1]:
                continue
            # 因为数组是有序的，如果两数之和大于目标值，右指针需要往左移动，而左指针不能动(在外层for left in range时进行枚举)
            while left < right and nums[left] + nums[right] > target:
                right -= 1
            # 需要考虑退出while循环时右指针可能会往左移动一格
            if left == right:
                break
            if nums[left] + nums[right] == target:
                result.append([nums[i], nums[left], nums[right]])
    return result


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([2, 7, 11, 15], []),
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
    ]

    def test(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, three_sum_equal_zero(nums))
