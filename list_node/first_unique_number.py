import unittest
from typing import List, Optional, Dict, Set


class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.prev: Optional[ListNode] = None
        self.next: Optional[ListNode] = None


class FindUnique:
    def __init__(self):
        self.head: ListNode = ListNode(-1)
        self.tail: ListNode = self.head
        # HashMap<Integer, ListNode>，可以在O(1)的时间内定位到重复元素在链表中的哪个节点，如果出现重复则把它删掉然后放到self.duplicate_nums中
        self.linked_list_index: Dict[int, ListNode] = dict()
        self.duplicate_nums: Set[int] = set()

    def add(self, num: int):
        if num in self.linked_list_index:
            need_to_remove = self.linked_list_index.get(num)
            need_to_remove.prev.next = need_to_remove.next
            self.duplicate_nums.add(num)
        else:
            new_node = ListNode(num)
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
        ([1, 2, 2, 1, 3, 4, 4, 5, 6], 5, 3),
        ([1, 2, 2, 1, 3, 4, 4, 5, 6], 7, -1),
        ([1, 2, 2, 1, 3, 4], 3, 3)
    ]

    def test_solution(self):
        for nums, end_num, first_unique in self.TEST_CASES:
            self.assertEqual(first_unique, solution(nums, end_num))
