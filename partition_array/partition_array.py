"""
[lintcode only]https://lintcode.com/problem/partition-array/
Input:
[3,2,2,1],2
Output:1
Explanation:
the real array is[1,2,2,3].So return 1

使用以下快速排序模板，没有我的解答快，因为有大量的下标访问越界判断
left, right = 0, len(nums) - 1
while left <= right:
    while left <= right and nums[left] < k:
        left += 1
    while left <= right and nums[right] >= k:
        right -= 1
    if left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
return left
"""

import unittest
from typing import List


# Your submission beats 88.20% Submissions!
def partition(nums: List[int], k: int) -> int:
    last_index = len(nums) - 1
    start, end = 0, last_index
    # FIXME 注意这里是start<=end
    while start <= end:
        if nums[start] >= k:
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1
            # 参考sort_color一题，交换过来的元素不确定是否小于2，所以start指针停在原地继续判断一次
        else:
            start += 1
    return start


def partition_template_2(nums: List[int], k: int) -> int:
    left, right = 0, len(nums) - 1
    # 类似某个二分或快速排序的模板，仅供partition，不容易获取题目要求的边界
    while left <= right:
        while left <= right and nums[left] <= k:
            left += 1
        while left <= right and nums[right] > k:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    print(nums)
    print("left", left, "right", right)
    return right-1


class Testing(unittest.TestCase):
    TESTCASES = [
        ([], 9, 0, []),
        ([3, 2, 2, 1], 2, 1, [1, 2, 2, 3]),
        ([7, 7, 9, 8, 6, 6, 8, 7, 9, 8, 6, 6], 10, 12, [7, 7, 9, 8, 6, 6, 8, 7, 9, 8, 6, 6]),
    ]

    def test(self):
        for nums, k, output, nums_after_partition in self.TESTCASES:
            partition_output = partition(nums, k)
            self.assertEqual(output, partition_output)
            self.assertEqual(nums_after_partition, nums)

    # def test_partition_template_2(self):
    #     for nums, k, output, nums_after_partition in self.TESTCASES:
    #         partition_output = partition_template_2(nums, k)
    #         self.assertEqual(output, partition_output)
    #         self.assertEqual(nums_after_partition, nums)
