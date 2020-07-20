import unittest
from typing import List


def deal_three_sum(nums: List[int], target: int, start: int, size: int, result: List[List[int]]):
    for i in range(start, size - 2):
        # 核心代码: i > start 注意去重的前提是i在第二次遍历时才比较
        # https://leetcode-cn.com/problems/4sum/solution/python-shuang-zhi-zhen-fa-zhu-yi-jian-zhi-yi-ji-pa/
        if i > start and nums[i] == nums[i-1]:
            continue
        left, right = i + 1, size - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if three_sum == target:
                # if [nums[start - 1], nums[i], nums[left], nums[right]] not in result:
                #     result.append([nums[start - 1], nums[i], nums[left], nums[right]])
                result.append([nums[start - 1], nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif three_sum < target:
                left += 1
            else:
                right -= 1
    return result


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    nums = sorted(nums)
    size = len(nums)
    result = []
    # 如果数组中的最小4项大于target，则往后的只会更大
    if sum(nums[:4]) > target:
        return []
    sum_of_last_3 = sum(nums[size-3:])
    for i in range(size - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 如果固定数+最大的后三项都小于target，则以固定数开头的组合不可能有候选项
        if nums[i] + sum_of_last_3 < target:
            continue
        deal_three_sum(nums, target - nums[i], i + 1, size, result)
    return result


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([1, 0, -1, -1, -1, -1, 0, 1, 1, 1, 2], 2, [[-1, 0, 1, 2], [-1, 1, 1, 1], [0, 0, 1, 1]]),
        ([2, 7, 11, 15], 3, []),
        ([1, 0, -1, 0, -2, 2], 0, [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]])
    ]

    def test_four_sum(self):
        for nums, target, expected in self.TEST_CASES:
            self.assertEqual(expected, four_sum(nums, target))
