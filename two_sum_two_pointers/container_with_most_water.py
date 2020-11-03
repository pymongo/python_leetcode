from typing import List


# 有点贪心的思想，相向双指针，移动较小的值，总能找到最大面积
class Solution:
    # noinspection PyPep8Naming
    @staticmethod
    def maxArea(nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        max_area = 0
        while left < right:
            width = right - left
            if nums[left] < nums[right]:
                area = nums[left] * width
                left += 1
            else:
                area = nums[right] * width
                right -= 1
            if area > max_area:
                max_area = area
        return max_area
