# https://leetcode.com/problems/odd-even-linked-list/
# 本题要求将奇数下标索引而非奇数值的链表节点挪到前面
# 有点像两个点旋转往前的音乐游戏
import unittest
from .list_node import ListNode


class Solution(unittest.TestCase):
    @staticmethod
    def f(head: ListNode) -> ListNode:
        if head is None:
            return None
        odd, even = head, head.next
        even_head = even
        while even and even.next:
            # 2(o)->1(e)->3->5 => 2->3(o)->5->1(e)
            odd.next = even.next
            odd = odd.next

            # 2->3(o)->5->1(e) => 2->3(o) 6<-5<-1(e)
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

    def test(self):
        test_cases = [
            ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4])
        ]
        for input_data, output in test_cases:
            self.assertListEqual(self.f(ListNode.from_list(input_data)).to_list(), output)
