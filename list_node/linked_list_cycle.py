from .list_node import ListNode


# 这道题面试要求O(1)空间复杂度，所以不能像first_unique_number这题一样用HashMap记录链表节点
class Solution:
    @staticmethod
    def is_cycle(head: ListNode) -> bool:
        """
        小学的操场追击问题: 只有链表内有环，慢指针一定能
        """
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    @staticmethod
    def find_cycle(head: ListNode):
        pass
