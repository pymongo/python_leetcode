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
        self.n: int = len(self.nums)
        if self.n > 0:
            self.heapify()

    def push(self, val: int):
        # old_len = insert_element_index
        insert_element_index = self.n
        self.nums.append(val)
        self.n += 1
        self._sift_up(insert_element_index)

    def pop(self) -> int:
        if self.n == 0:
            return -1
        last_index = self.n - 1
        self.nums[0], self.nums[last_index] = self.nums[last_index], self.nums[0]
        output = self.nums.pop()
        self.n -= 1
        self._sift_down(0)
        return output

    # 平均O(n)时间复杂度
    def heapify(self):
        """
        根据堆(完全二叉树)的左儿子公式 i * 2 + 2
        假设数组最后索引为len-1, len-1 = i*2+1 => i = len//2 -1
        所以最深的左叶子节点的根的下标是len//2 - 1，就算最后一个是右儿子根据地板除的规律，也能得到最后一个最深左叶子节点的根的索引
        从最深左叶子节点的根开始往上sift_down(比较当前节点和左右儿子的最大值)调整
        """
        for i in range(self.n // 2 - 1, -1, -1):
            self._sift_down(i)

    # TODO Python的siftup是跟儿子比，Rust的siftup是跟父节点比，Rust的更加正确
    def _sift_up(self, curr: int):
        """
        只比较当前节点和父亲节点之前的最大值，如果发生挪到，则curr=parent
        之所以叫up是因为迭代过程会不断往二叉树的顶部走
        FIXME 只有push的时候用得到，除了push其余操作基本是用sift_down, push时用sift_up比sift_down快
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
        while curr < self.n:
            left_child = 2 * curr + 1
            right_child = left_child + 1
            max_index = curr
            if left_child < self.n and self.nums[left_child] > self.nums[max_index]:
                max_index = left_child
            if right_child < self.n and self.nums[right_child] > self.nums[max_index]:
                max_index = right_child
            if max_index == curr:
                break
            self.nums[curr], self.nums[max_index] = self.nums[max_index], self.nums[curr]
            curr = max_index


class HeapRecipe:
    def __init__(self, nums: List[int] = None):
        if nums is not None:
            self.n = len(nums)
            self.nums = nums
            self.heapify()
        else:
            self.n = 0
            self.nums = []

    def push(self, val: int):
        self.nums.append(val)
        self.n += 1
        self.sift_up(self.n - 1)

    def pop(self) -> int:
        if self.n == 0:
            return -1
        self.nums[0], self.nums[self.n - 1] = self.nums[self.n - 1], self.nums[0]
        res = self.nums.pop()
        self.n -= 1
        self.sift_down(0)
        return res

    def heapify(self):
        for i in range(self.n // 2 - 1, -1, -1):
            self.sift_down(i)

    def sift_down(self, index: int):
        while index < self.n:
            left = 2 * index + 1
            right = left + 1
            max_index = index
            if left < self.n and self.nums[left] > self.nums[max_index]:
                max_index = left
            if right < self.n and self.nums[right] > self.nums[max_index]:
                max_index = right
            if max_index == index:
                break
            # FIXME 默写时漏掉下面这行
            self.nums[index], self.nums[max_index] = self.nums[max_index], self.nums[index]
            index = max_index

    def sift_up(self, index: int):
        # FIXME 这里是index>0
        while index > 0:
            parent = (index - 1) // 2
            # FIXME 这里不用判越界parent最低只能是0
            if self.nums[parent] >= self.nums[index]:
                break
            self.nums[parent], self.nums[index] = self.nums[index], self.nums[parent]
            index = parent


class TestMyHeap(unittest.TestCase):
    def test_push_pop(self):
        heap = HeapRecipe()
        for num in (3, 5, 4, 7):
            heap.push(num)
        self.assertListEqual([7, 5, 4, 3], heap.nums)
        res = []
        for _ in range(heap.n):
            res.append(heap.pop())
        self.assertListEqual([7, 5, 4, 3], res)

    def test_heapify(self):
        nums = [4, 10, 3, 5, 1, 2]
        heap = HeapRecipe(nums.copy())
        sorted_nums = []
        for _ in range(heap.n):
            sorted_nums.append(heap.pop())
        self.assertListEqual(sorted_nums, sorted(nums, reverse=True))
