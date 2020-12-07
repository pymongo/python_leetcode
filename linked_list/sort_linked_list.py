# https://leetcode.com/problems/insertion-sort-list/
# 其实就是让你对链表进行排序，对链表来说最高效的排序是归并排序
import unittest
from .list_node import ListNode


class Solution(unittest.TestCase):
    @staticmethod
    def f(head: ListNode) -> ListNode:
        pass

    def test(self):
        test_cases = [
            ([4, 2, 1, 3], [1, 2, 3, 4])
        ]
        for input_data, output in test_cases:
            self.assertListEqual(self.f(ListNode.from_list(input_data)).to_list(), output)
