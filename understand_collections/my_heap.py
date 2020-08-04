import unittest
from typing import List


# max-heap
class MyHeap:
    def __init__(self, nums: List[int] = None):
        self.nums: List[int] = [] if nums is None else nums
        self.len: int = len(self.nums)

    def push(self, val: int):
        # old_len = insert_element_index
        insert_element_index = self.len
        self.nums.append(val)
        self.len += 1
        self._sift_up(insert_element_index)

    def pop(self):
        pass

    def heapify(self):
        pass

    def _sift_up(self, pos: int):
        while pos > 0:
            parent = (pos - 1) // 2
            if self.nums[parent] >= self.nums[pos]:
                break
            self.nums[parent], self.nums[pos] = self.nums[pos], self.nums[parent]
            pos = parent

    def _sift_down(self):
        pass


class TestMyHeap(unittest.TestCase):
    def test_push_pop(self):
        heap = MyHeap()
        heap.push(3)
        heap.push(5)
        heap.push(4)
        heap.push(7)
        print(heap.nums)
