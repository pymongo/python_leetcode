"""
https://leetcode.com/problems/3sum/
判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组
不重复意味着[1,1,0,-1]中只有一组解，用第一个1和第二个1组成的解视为一个
模式识别: 利用排序避免重复的解
"""

import unittest
from typing import List
from copy import deepcopy


class Solution(unittest.TestCase):
    TWO_SUM_PLANS_DETAILS_TEST_CASES = [
        ([1, 1, 2, 3, 4, 5], 6, [[1, 5], [2, 4]])
    ]

    # 字节跳动喜欢考枚举Two Sum每个方案的详情，我看leetcode没有原题，类似的有three-sum，所以还是自己写测试用例练一练
    def test_two_sum_plans_detail(self):
        for nums, target, plans_detail in self.TWO_SUM_PLANS_DETAILS_TEST_CASES:
            self.assertListEqual(plans_detail, self.two_sum_plans_detail(nums, target))

    @staticmethod
    def two_sum_plans_detail(nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        left, right = 0, n - 1
        while left < right:
            # 去重
            if left > 0 and nums[left] == nums[left-1]:
                left += 1
                continue
            if right < n-1 and nums[right] == nums[right-1]:
                right -= 1
                continue

            two_sum = nums[left] + nums[right]
            if two_sum > target:
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
        return res


def three_sum_equal_zero(nums: List[int]) -> List[List[int]]:
    results = []
    # 通过shadowing重新赋值的好处是排序时不会修改掉原来的nums数组
    nums = sorted(nums)
    length = len(nums)
    last_index = length - 1
    for i in range(length):
        # 从小到大搜索，跳过重复值
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        right = last_index
        target = -nums[i]
        for left in range(i + 1, length):
            if left > i + 1 and nums[left] == nums[left - 1]:
                continue
            # 因为数组是有序的，如果两数之和大于目标值，右指针需要往左移动，而左指针不能动(在外层for left in range时进行枚举)
            while left < right and nums[left] + nums[right] > target:
                right -= 1
            # 需要考虑退出while循环时右指针可能会往左移动一格
            if left == right:
                break
            if nums[left] + nums[right] == target:
                results.append([nums[i], nums[left], nums[right]])
    return results


# Your submission beats 98.20% Submissions!
def three_sum_second_try(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []
    nums = sorted(nums)
    size = len(nums)
    results = []

    for i in range(size - 2):
        # i的去重不能依赖于two_sum==target的分支内
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, size - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if three_sum == 0:
                results.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif three_sum < 0:
                left += 1
            else:
                right -= 1
    return results


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([2, 7, 11, 15], []),
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
    ]

    def test(self):
        for nums, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, three_sum_equal_zero(nums))

    def test_three_second_try(self):
        for nums, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, three_sum_second_try(nums))
