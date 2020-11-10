from typing import List
import unittest


# def find_minimum_value_in_rotated_sorted_array(nums: List[int]) -> int:
#     start, end = 0, len(nums) - 1
#     while start < end:
#         middle = start + (end - start) // 2
#         # 比较中间和右边
#         if nums[middle] < nums[end]:
#             end = middle
#         else:
#             # [3,4,5,1,2], nums[middle]=5, start需要前移, nums[middle]已经是最大值了，所以要start前移到middle+1的位置
#             # 如果不知道二分的边界变化，找一个例子代入进去试试就好
#             # 大于等于或小于等于的二分分支可以start=middle+1或end=middle-1
#             start = middle + 1
#     return nums[start]

# 与无重复找最小值的区别是 多了一个nums[mid]==nums[end]的分支，其余情况基本一致
def min_of_rotated_sorted(nums: List[int]) -> int:
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + (end - start) // 2
        if nums[mid] > nums[end]:
            start = mid + 1
        elif nums[mid] < nums[end]:
            # 保守起见end = mid
            end = mid
        else:
            # 有可能是U型情况，保守起见end -= 1
            end -= 1
    return nums[start]


class Testing(unittest.TestCase):
    TEST_CASES = [
        [1, 3, 5],
        [2, 2, 2, 0, 1],
    ]

    def test_min_of_rotated_sorted(self):
        for nums in self.TEST_CASES:
            self.assertEqual(min(nums), min_of_rotated_sorted(nums))
