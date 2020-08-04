import unittest
from typing import List, Optional, Dict, Set


class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: Optional[ListNode] = None


class FindUnique:
    def __init__(self):
        self.head: ListNode = ListNode(-1)
        self.tail: ListNode = self.head
        # HashMap<Integer, ListNode>，存储节点num的上一个节点，方便删除操作
        # 如果出现重复则把它删掉然后放到self.duplicate_nums中
        self.linked_list_prev: Dict[int, ListNode] = dict()
        self.duplicate_nums: Set[int] = set()

    def add(self, num: int):
        if num in self.duplicate_nums:
            return
        if num in self.linked_list_prev:
            # 注意要删掉num在linked_list_prev的节点
            duplicate_prev = self.linked_list_prev.pop(num)
            duplicate_prev.next = duplicate_prev.next.next
            self.duplicate_nums.add(num)
        else:
            new_node = ListNode(num)
            self.linked_list_prev[num] = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def get_first_unique(self):
        if self.head.next is None:
            return -1
        return self.head.next.val


def solution(nums: List[int], end_num: int) -> int:
    find_unique = FindUnique()
    for num in nums:
        find_unique.add(num)
        if num == end_num:
            return find_unique.get_first_unique()
    return -1


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 2, 1, 3, 4], 3, 3),
        ([1, 2, 2, 1, 3, 4, 4, 5, 6], 5, 3),
        ([1, 2, 2, 1, 3, 4, 4, 5, 6], 7, -1),
    ]

    def test_solution(self):
        for nums, end_num, first_unique in self.TEST_CASES:
            self.assertEqual(first_unique, solution(nums, end_num))
