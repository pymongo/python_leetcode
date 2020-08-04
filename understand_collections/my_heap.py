import unittest
from typing import List


# max-heap
class MyHeap:
    """
    i's parent: (i - 1) // 2
    i's left  :  i * 2 + 1
    i's right :  i * 2 + 2
    """

    def __init__(self, nums: List[int] = None):
        self.nums: List[int] = [] if nums is None else nums
        self.len: int = len(self.nums)

    def push(self, val: int):
        # old_len = insert_element_index
        insert_element_index = self.len
        self.nums.append(val)
        self.len += 1
        self._sift_up(insert_element_index)

    def pop(self) -> int:
        if self.len == 0:
            return -1
        last_index = self.len - 1
        self.nums[0], self.nums[last_index] = self.nums[last_index], self.nums[0]
        output = self.nums.pop()
        self.len -= 1
        print(self.nums)
        self._sift_down(0)
        return output

    def heapify(self):
        """
        根据堆(完全二叉树)的左儿子公式 i * 2 + 2
        假设数组最后索引为len-1, len-1 = i*2+1 => i = len//2 -1
        所以最深的左叶子节点的根的下标是len//2 - 1，就算最后一个是右儿子根据地板除的规律，也能得到最后一个最深左叶子节点的根的索引
        从最深左叶子节点的根开始往上sift_down(比较当前节点和左右儿子的最大值)调整
        """
        for i in range(self.len // 2 - 1, -1, -1):
            self._sift_down(i)

    def _sift_up(self, curr: int):
        """
        只比较当前节点和父亲节点之前的最大值，如果发生挪到，则curr=parent
        之所以叫up是因为迭代过程会不断往二叉树的顶部走
        FIXME 如果已经是max-heap, push时用sift_up比sift_down快多了，新增元素用sift_down也可以，不过用sift_up效率高
        """
        while curr > 0:
            parent = (curr - 1) // 2
            if self.nums[parent] >= self.nums[curr]:
                break
            self.nums[parent], self.nums[curr] = self.nums[curr], self.nums[parent]
            curr = parent

    def _sift_down(self, curr: int):
        """
        只比较当前节点和左右儿子，如果发生挪到，则curr=变动的左/右儿子
        之所以叫down是因为迭代过程会不断往二叉树的底部
        FIXME 如果是heapify一个乱序数组，那么只能用sift_down去调整，因为sift_up只比较curr和parent，不会比left和right
        FIXME 由于pop操作是顶部元素，所以只能往下调整(sift_down)
        """
        while curr < self.len:
            left_child = 2 * curr + 1
            right_child = left_child + 1
            max_index = curr
            if left_child < self.len and self.nums[left_child] > self.nums[max_index]:
                max_index = left_child
            if right_child < self.len and self.nums[right_child] > self.nums[max_index]:
                max_index = right_child
            if max_index == curr:
                break
            self.nums[curr], self.nums[max_index] = self.nums[max_index], self.nums[curr]
            curr = max_index


class TestMyHeap(unittest.TestCase):
    def test_push_pop(self):
        heap = MyHeap()
        heap.push(3)
        heap.push(5)
        heap.push(4)
        heap.push(7)
        print(heap.nums)
        for _ in range(heap.len):
            print(heap.pop())

