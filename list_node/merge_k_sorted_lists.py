import unittest
from .list_node import ListNode


class Solution(unittest.TestCase):
    TEST_CASES = [
        ("1->2->4", "1->3->4", "1->1->2->3->4->4"),
    ]

    def test(self):
        for l1, l2, output in self.TEST_CASES:
            self.assertEqual(output, self.merge(ListNode.from_str(l1), ListNode.from_str(l2)).__str__())

    @staticmethod
    def merge(l1: ListNode, l2: ListNode) -> ListNode:
        new_ln_head = ListNode(0)
        curr = new_ln_head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return new_ln_head.next

