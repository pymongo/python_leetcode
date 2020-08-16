"""
Input: list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)]
Output: [(1,4),(5,6)]
Explanation:
(1,2),(2,3),(3,4) --> (1,4)
(5,6) --> (5,6)
"""
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# 类似两个小水滴💧合并成一个大水滴的感觉
# 除了合并间隔，leetcode还要一题要求间隔交集(未做)986. Interval List Intersections
class Solution:
    @staticmethod
    def f(list1: List[Interval], list2: List[Interval]) -> List[Interval]:
        # 用一个 last 来记录最后一个还没有被放到 merge results 里的 Interval，用于和新加入的 interval 比较看看能不能合并到一起
        i, j, res = 0, 0, []
        m, n = len(list1), len(list2)
        while i < m and j < n:
            if list1[i].start < list2[j].start:
                Solution.push_back(res, list1[i])
                i += 1
            else:
                Solution.push_back(res, list2[j])
                j += 1

        while i < m:
            Solution.push_back(res, list1[i])
            i += 1
        while j < n:
            Solution.push_back(res, list2[j])
            j += 1
        return res

    @staticmethod
    def push_back(intervals: List[Interval], new_interval: Interval):
        if not intervals:
            intervals.append(new_interval)
            return

        last_interval = intervals[-1]
        # 没有交集的情况
        if last_interval.end < new_interval.start:
            intervals.append(new_interval)
            return

        last_interval.end = max(last_interval.end, new_interval.end)

    @staticmethod
    def merge_k(a):
        n = len(a)
        if n == 0:
            return []
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                a[i] = Solution.f(a[i], a[i + interval])
            interval *= 2
        return a[0]
