"""
https://leetcode.com/problems/reverse-linked-list/
"""

from .list_node import ListNode
import unittest


def reverse_linked_list(head: ListNode) -> ListNode:
    pre = None
    cur = head
    # 退出循环时，刚好pre是逆序链表的第一个节点，cur是原链表最后一个节点的next(None)
    while cur is not None:
        # 临时保存cur指向原链表下一个节点的链接，用于pre移到cur,cur移到next
        temp_next = cur.next
        # 切断cur指向原链表下一个元素的链接，改为连向pre
        cur.next = pre
        # pre和cur往前挪
        pre = cur
        cur = temp_next
    return pre


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3], [3, 2, 1])
    ]

    def test(self):
        for nums, expected in self.TEST_CASES:
            list_node = ListNode.from_list(nums)
            self.assertEqual(expected, reverse_linked_list(list_node).to_list())
