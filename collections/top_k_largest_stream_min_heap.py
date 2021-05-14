"""
数据流中位数    http://www.lintcode.com/problem/data-stream-median/
数据流最大 K 项 http://www.lintcode.com/problem/top-k-largest-numbers-ii/
数据流高频 K 项 http://www.lintcode.com/problem/top-k-frequent-words-ii/
"""
import unittest
import heapq
from typing import List

# https://lintcode.com/problem/top-k-largest-numbers/
def topk(self, nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    for num in nums[k:]:
        heapq.heappushpop(min_heap, num)
    min_heap.sort()
    return min_heap[::-1]

class TopKLargestNums:
    def __init__(self, k: int):
        self.k = k
        self.nums = []
        self.size = 0

    def add(self, val: int):
        if self.size < self.k:
            heapq.heappush(self.nums, val)
            self.size += 1
        else:
            heapq.heappushpop(self.nums, val)

    def topk(self) -> List[int]:
        # 一个升序的数组是「完美小根堆」
        self.nums.sort()
        return self.nums[::-1]


class Testing(unittest.TestCase):
    def test_kth_largest_element_in_a_stream(self):
        h = MinHeap(1, [-2])
        print(h.add_703(-3))
        print(h.add_703(0))
        print(h.add_703(2))
        print(h.add_703(-1))
        print(h.add_703(4))

    def test_top_k_largest_numbers(self):
        h = MinHeap(3)
        h.add(3)
        h.add(10)
        print(h.topk())
        h.add(1000)
        print(h.nums)
