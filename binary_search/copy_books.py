import unittest
from typing import List


# 本题跟longest_increase_subsequence类似
# TODO 工时类动态规划、最大工时价值?
# 直观的做法是动态规划，而巧妙的做法是贪心+二分
# 给定一个任务耗时的数组，以及人数，每个人不能跳着做任务，求完成所有任务的耗时这类问题就是其中一种动态规划的经典题型
# 为什么能用缩短答案集的规律?
# 假设最短完成耗时是x，人数是y，随着x不断减小，y会有一个临界值刚好等于人数k，往后x再增大的时候人数会大于k，答案集二分的题例如woods-cut都有类似的感觉
class Solution(unittest.TestCase):
    TEST_CASES = [
        ([3, 2, 4], 2, 5),
        ([3, 2, 4], 3, 4),
    ]

    def test_binary_search(self):
        for nums, k, cost_time in self.TEST_CASES:
            self.assertEqual(cost_time, self.binary_search(nums, k))

    @staticmethod
    def binary_search(nums: List[int], k: int) -> int:
        size = len(nums)
        if size == 0:
            return 0

        # 通过最大人均工时推算需要参与的人数
        def get_number_of_peoples(time_limit: int) -> int:
            # 人数的可能范围是: 1..=n
            n_peoples = 1
            last_people_work_time = 0
            for num in nums:
                if last_people_work_time + num > time_limit:
                    n_peoples += 1
                    last_people_work_time = 0
                last_people_work_time += num
            return n_peoples

        # start和end表示最短完成耗时，去搜索答案集为k人的答案
        # max(nums)表示最快用len(nums)个人一人抄一本书也要最短耗费max(nums)的时间
        # sum(nums)表示最慢情况用1个人抄完所有的书
        # 所以越往start走，耗时会最短，所以这里用find_first的二分模板找到「第一个」人数=k的方案
        total = 0
        max_num = 0
        for num in nums:
            max_num = max(max_num, num)
            total += num
        start, end = max_num, total
        # start, end = max(nums), sum(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if get_number_of_peoples(mid) <= k:
                end = mid
            else:
                start = mid
        if get_number_of_peoples(start) <= k:
            return start
        return end
