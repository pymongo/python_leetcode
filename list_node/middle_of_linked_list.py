"""
链表的中位数，有两种题型:
1. 返回左中位数的值，[lintcode 228. Middle of Linked List](https://www.lintcode.com/problem/middle-of-linked-list/description?_from=ladder&&fromId=161)
2. 从右中位数开始截断链表，返回链表右中位数到末尾的部分(https://leetcode.com/problems/middle-of-the-linked-list/)
"""

from .list_node import ListNode
import unittest


# 返回链表右中位数到末尾的部分
def middle_of_the_linked_list(list_node: ListNode) -> ListNode:
    return ListNode(-1)


# 返回链表的左中位数
def middle_of_linked_list(list_node: ListNode) -> int:
    nums = [list_node.val]
    length = 1
    curr_node = list_node
    while curr_node.next is not None:
        curr_node = curr_node.next
        nums.append(curr_node.val)
        length += 1
    return nums[(length-1) // 2]


class UnitTest(unittest.TestCase):
    TEST_CASES_MIDDLE_OF_THE_LINKED_LIST = [

    ]
    TEST_CASES_MIDDLE_OF_LINKED_LIST = [
        ([1, 2, 3], 2)
    ]

    def test_middle_of_the_linked_list(self):
        for nums, expected in self.TEST_CASES_MIDDLE_OF_LINKED_LIST:
            list_node = ListNode.from_list(nums)
            self.assertEqual(expected, middle_of_linked_list(list_node))
