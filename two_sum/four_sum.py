import unittest
from typing import List


def deal_three_sum(nums: List[int], target: int, start: int, result: List[List[int]]):
    size = len(nums)
    for i in range(start, size - 2):
        # 这里去重会漏掉解惑重复解
        # if nums[i] == nums[i+1]:
        #     continue
        left, right = i + 1, size - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if three_sum == target:
                # 暂时先用这种笨方法去重
                if [nums[start - 1], nums[i], nums[left], nums[right]] not in result:
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
    if not nums:
        return []
    nums = sorted(nums)
    size = len(nums)
    result = []
    for i in range(size - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        deal_three_sum(nums, target - nums[i], i + 1, result)
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
