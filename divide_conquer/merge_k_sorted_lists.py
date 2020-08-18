import unittest
from typing import List, Optional
from list_node.list_node import ListNode
import heapq


# 用于优先队列比较
class NodeWrapper:
    def __init__(self, list_node):
        # 参考了Rust的actix_web::web::Data<T>
        self.inner = list_node

    def __lt__(self, other):
        return self.inner.val < other.inner.val


class Solution(unittest.TestCase):
    MERGE_TWO_LISTS_CASES = [
        ("1->2->4", "1->3->4", "1->1->2->3->4->4"),
    ]

    def test(self):
        for l1, l2, output in self.MERGE_TWO_LISTS_CASES:
            self.assertEqual(output, self.merge_two_lists(ListNode.from_str(l1), ListNode.from_str(l2)).__str__())

    @staticmethod
    def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
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

    # 调用合并两个有序链表的方法，reduce的思想去两两合并，leetcode垫底，lintcode超时
    # 由于至少需要合并k-1次，能否均匀一些，参考归并排序，两两合并，最后只需要logk次
    @staticmethod
    def merge_k_one_by_one(lists: List[ListNode]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        last = lists[0]
        for i in range(1, n):
            last = Solution.merge_two_lists(last, lists[i])
        return last

    @staticmethod
    def merge_sort_k_lists(lists: List[ListNode]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        # 1<-2 3<-4
        # 1 <- 3
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = Solution.merge_two_lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    @staticmethod
    def heapq_solution(lists: List[ListNode]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        # 长度固定为k的优先队列
        heap = []
        for i in range(k):
            if lists[i] is None:
                continue
            heapq.heappush(heap, NodeWrapper(lists[i]))

        dummy = ListNode(0)
        curr = dummy
        while heap:
            wrapper = heapq.heappop(heap)
            curr.next = wrapper.inner
            curr = curr.next
            if wrapper.inner.next is not None:
                wrapper.inner = wrapper.inner.next
                heapq.heappush(heap, wrapper)
        return dummy.next
