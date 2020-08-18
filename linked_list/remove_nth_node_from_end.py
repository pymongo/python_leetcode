from .list_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 用dummy的好处是能应对删掉头结点的测试用例
        dummy = ListNode(0)
        dummy.next = head

        # 长度为n的滑动窗口，当窗口滑到底时，left指针正好是倒数第n个节点
        left, right = dummy, dummy
        for _ in range(n):
            right = right.next

        while right.next:
            left, right = left.next, right.next

        left.next = left.next.next
        return dummy.next
