import unittest
import heapq
from typing import List


# min-heap
class MinHeap:
    """
    为什么用小根堆?
    「末尾淘汰制度」的思想，堆里面至多有k个元素，新来的元素至少要击败其中一个，才能进入堆
    说是小根堆，实际上存的是最大的几个，类似福布斯富豪榜，新来的必须足够大才能上榜
    """

    def __init__(self, k: int, nums: List[int] = None):
        self.nums: List[int] = [] if nums is None else nums
        self.len: int = len(self.nums)
        self.k: int = k
        self.is_full: bool = False
        if self.len > 0:
            self.heapify()
            if self.len >= k:
                self.is_full = True
                for _ in range(self.len - self.k):
                    self.pop()
                self.len = k

    # leetcode.703. Kth Largest Element in a Stream
    def add_703(self, val: int) -> int:
        self.push(val)
        return self.nums[0]

    def add(self, val: int):
        self.push(val)

    def topk(self) -> List[int]:
        old_nums = self.nums.copy()
        old_len = self.len
        result = []
        for _ in range(self.k if self.is_full else self.len):
            result.insert(0, self.pop())
        self.nums = old_nums
        self.len = old_len
        return result

    def push(self, val: int):
        if self.is_full:
            if val <= self.nums[0]:
                # 新来的比强者榜上最小的还要小
                return
            # 以下过程等同于heapq.heapreplace
            insert_element_index = self.len
            self.nums.append(val)
            self.len += 1
            self._sift_up(insert_element_index)
            self.pop()
            return
        insert_element_index = self.len
        self.nums.append(val)
        self.len += 1
        if self.len == self.k:
            self.is_full = True
        self._sift_up(insert_element_index)

    def pop(self) -> int:
        if self.len == 0:
            return -1
        last_index = self.len - 1
        self.nums[0], self.nums[last_index] = self.nums[last_index], self.nums[0]
        output = self.nums.pop()
        self.len -= 1
        self._sift_down(0)
        return output

    def heapify(self):
        for i in range(self.len // 2 - 1, -1, -1):
            self._sift_down(i)

    # 如果已经是min-heap, push时用sift_up比sift_down快多了，新增元素用sift_down也可以，不过用sift_up效率高
    def _sift_up(self, curr: int):
        while curr > 0:
            parent = (curr - 1) // 2
            if self.nums[parent] <= self.nums[curr]:
                break
            self.nums[parent], self.nums[curr] = self.nums[curr], self.nums[parent]
            curr = parent

    # 如果是heapify一个乱序数组，那么只能用sift_down去调整，因为sift_up只比较curr和parent，不会比left和right，由于pop操作是顶部元素，所以只能往下调整(sift_down)
    def _sift_down(self, curr: int):
        while curr < self.len:
            left_child = 2 * curr + 1
            right_child = left_child + 1
            min_index = curr
            if left_child < self.len and self.nums[left_child] < self.nums[min_index]:
                min_index = left_child
            if right_child < self.len and self.nums[right_child] < self.nums[min_index]:
                min_index = right_child
            if min_index == curr:
                break
            self.nums[curr], self.nums[min_index] = self.nums[min_index], self.nums[curr]
            curr = min_index


class TopKLargestNums:
    """ 544. Top k Largest Numbers
    def topk(self, nums, k):
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for num in nums[k:]:
            heapq.heappushpop(min_heap, num)
        min_heap.sort()
        return min_heap[::-1]
    """
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
