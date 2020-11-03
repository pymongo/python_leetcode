"""
https://leetcode.com/problems/reverse-linked-list/
"""

from .list_node import ListNode
import unittest
from typing import Optional


class Solution(unittest.TestCase):
    def test_reverse_list_1(self):
        TESTCASES = [
            ([1, 2, 3], [3, 2, 1]),
        ]
        for nums, expected in TESTCASES:
            list_node = ListNode.from_list(nums)
            self.assertEqual(expected, self.reverse_list_1(list_node).to_list())

    @staticmethod
    def reverse_list_1(head: ListNode) -> Optional[ListNode]:
        if head is None:
            return None
        # new表示已反转的链表的最后一个节点
        new = None
        # old表示未反转部分的第一个节点
        old = head
        # 退出循环时，刚好pre是逆序链表的第一个节点，cur是原链表最后一个节点的next(None)
        while old:
            successor = old.next
            old.next = new

            new = old
            old = successor
        return new

    def test_reverse_list_2(self):
        TESTCASES = [
            ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ]
        for nums, m, n, expected in TESTCASES:
            list_node = ListNode.from_list(nums)
            self.assertEqual(expected, self.reverse_range(list_node, m, n).to_list())

    # 反转链表(m, n)部分可以理解为将head前移到位置m，然后调用以下的反转前n个节点的函数
    @staticmethod
    def reverse_range(head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        # 从dummy开始计数，保证节点能从1开始编号，所以dummy前移m-1次的节点就是需要反转开始位置的前一个节点
        node_m_prev = dummy
        for _ in range(m - 1):
            node_m_prev = node_m_prev.next
        # rev_head需要反转部分的头部(会不断前移)
        # rev_prev第一次反转时的头部的前驱节点
        rev_head = node_m_prev.next

        """ 方框表示rev_head
        Phase 1. 将(3)扔到1和2中间
        1 [2 (3) 4 5]
         ^
        Phase 2. 将(4)扔到1和3中间
        1 3 [2 (4) 5]
         ^
        """
        for _ in range(m, n):
            # 备份rev_head.next
            rev_head_next = rev_head.next
            # rev_head的next指针越过rev_head_next，做好将rev_head_next扔掉的准备
            rev_head.next = rev_head_next.next
            # rev_head_next插入到node_m_prev和node_m_prev.next之间
            rev_head_next.next = node_m_prev.next
            node_m_prev.next = rev_head_next
        return dummy.next
