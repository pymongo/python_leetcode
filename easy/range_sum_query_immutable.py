from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        # sum_range(0,2) = nums[2] - nums[-1]
        nums.append(0)
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j] - self.nums[i - 1]
