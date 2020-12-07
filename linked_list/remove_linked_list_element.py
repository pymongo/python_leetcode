from .list_node import ListNode
import unittest


# https://leetcode.com/problems/remove-linked-list-elements/
class Solution(unittest.TestCase):
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(-1)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next

    def test(self):
        head = ListNode.from_list([1, 2, 6, 3, 4, 5, 6])
        self.assertListEqual(self.removeElements(head, 6).to_list(), [1, 2, 3, 4, 5])
