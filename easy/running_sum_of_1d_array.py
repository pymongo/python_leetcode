from typing import List


def my_solution(nums: List[int]) -> List[int]:
    """
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
    """
    res = []
    rolling_sum = 0
    for num in nums:
        rolling_sum += num
        res.append(rolling_sum)
    return res


# O(1) Space
def best_solution(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    return nums
