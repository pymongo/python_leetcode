from .list_node import ListNode


class Solution:
    @staticmethod
    def bottom_up_plus_one(node: ListNode) -> int:
        if node is None:
            return 1
        carry = Solution.bottom_up_plus_one(node.next)
        if carry == 0:
            return 0
        if node.val == 9:
            node.val = 0
            return 1
        else:
            node.val += 1
            return 0

    @staticmethod
    def plus_one(head: ListNode) -> ListNode:
        carry = Solution.bottom_up_plus_one(head)
        if carry == 1:
            head = ListNode(1, head)
        return head
