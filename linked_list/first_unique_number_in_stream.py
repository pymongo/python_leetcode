import unittest
from .list_node import ListNode
from typing import List, Dict, Set


# 相似题型: LRU
# 所谓双向链表，指的是每个节点除了next指针外还有prev指针指向上一个节点
# 删除操作的单链表和双链表比较:
# 1. 单链表: 更新prev_map[delete_key].next，map删掉一项，被删节点是不是尾部 ? 更新尾指针 : 更新pre_map中被删节点的下一个节点的prev指针
# 2. 双链表: 头尾都有一个哑指针，map删掉一项，然后仅有两根指针要变，简单多了
# 只有删除或尾部插入，用单链表双链表都可以
# 如果像LRU这题需要频繁的挪动链表的节点，还是用更简单的双链表方便维护
class FindUnique:
    def __init__(self):
        self.head: ListNode = ListNode(-1)
        self.tail: ListNode = self.head
        # HashMap<Integer, ListNode>，存储节点num的上一个节点，方便删除操作
        # 如果出现重复则把它删掉然后放到self.duplicate_nums中
        # 这个HashMap的数据结构很妙，这样子就不用使用「双向链表」
        self.linked_list_prev: Dict[int, ListNode] = dict()
        self.duplicate_nums: Set[int] = set()

    def add(self, num: int):
        if num in self.duplicate_nums:
            return
        if num in self.linked_list_prev:
            # 注意要删掉num在linked_list_prev的节点
            duplicate_prev = self.linked_list_prev.pop(num)
            duplicate_prev.next = duplicate_prev.next.next
            # del duplicate_prev.next
            if duplicate_prev.next is None:
                # deleted node is tail of linked list, need to update self.tail
                self.tail = duplicate_prev
            else:
                # 需要更新被删除节点的下一个节点的prev指针
                self.linked_list_prev[duplicate_prev.next.val] = duplicate_prev
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
