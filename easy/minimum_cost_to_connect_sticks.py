import heapq


# 根据题意，考虑贪心，我们每次将所有棒材的最短的两根合并，将合并后的棒材放入棒材堆，重复合并最短的，直到棒材只剩下一根
class Solution:
    @staticmethod
    def minimum_cost(nums):
        res = 0
        heapq.heapify(nums)
        while len(nums) > 1:
            a, b = heapq.heappop(nums), heapq.heappop(nums)
            new_num = a + b
            res += new_num
            heapq.heappush(nums, new_num)
        # 最终堆剩余的一根棒就不需要继续合并了
        # if len(nums) == 1:
        #     res = res + (res + nums[0])
        return res
