import operator
from typing import List


# 这道题不看官方解答我都不知道题目的公式是什么意思，硬是靠测试用例慢慢改对
class Solution:
    def constructArr(self, nums: List[int]) -> List[int]:
        # product = functools.reduce(operator.mul, nums)
        product = 1
        zero_index = -1
        for i, num in enumerate(nums):
            if num == 0:
                if zero_index != -1:
                    # 如果第二个0出现
                    return [0] * len(nums)
                zero_index = i
                continue
            product *= num
        if zero_index != -1:
            res = [0] * len(nums)
            res[zero_index] = product
            return res
        else:
            return [product // num for num in nums]

    @staticmethod
    def best_solution(nums: List[int]) -> List[int]:
        # 这题要求不能用除法，可以理解为output[i]等于nums中除了nums[i]其余各项的乘积
        # 所以如果nums中有1个0，则除了0的下标，output的所有结果都为0
        # 如果有两个0，那就可以提前结束返回全为0的数组
        b, tmp = [1] * len(nums), 1
        for i in range(1, len(nums)):
            b[i] = b[i - 1] * nums[i - 1]  # 下三角
        for i in range(len(nums) - 2, -1, -1):
            tmp *= nums[i + 1]  # 上三角
            b[i] *= tmp  # 下三角 * 上三角
        return b
