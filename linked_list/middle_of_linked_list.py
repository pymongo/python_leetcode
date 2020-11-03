"""
链表的中位数，有两种题型:
1. 返回左中位数的节点，[lintcode 228. Middle of Linked List](https://www.lintcode.com/problem/middle-of-linked-list/description?_from=ladder&&fromId=161)
2. 从右中位数开始截断链表，返回链表右中位数到末尾的部分(https://leetcode.com/problems/middle-of-the-linked-list/)
TODO 链表题型的快慢双指针算法
快指针每次两步，慢指针每次一步
快指针到尾的时候，慢指针就是中点(左中位节点)
"""

from .list_node import ListNode
import unittest
from typing import Optional


# 返回链表右中位数到末尾的部分
def middle_of_the_linked_list(list_node: ListNode) -> ListNode:
    slow = list_node
    fast = list_node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


# 通过快慢双指针算法 返回链表的左中位数节点
def middle_of_linked_list(list_node: ListNode) -> Optional[ListNode]:
    if list_node is None:
        return None
    slow, fast = list_node, list_node.next
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
    return slow


# 返回链表的左中位数
def middle_of_linked_list_brute_force(list_node: ListNode) -> int:
    nums = [list_node.val]
    length = 1
    curr_node = list_node
    while curr_node.next is not None:
        curr_node = curr_node.next
        nums.append(curr_node.val)
        length += 1
    return nums[(length - 1) // 2]


class UnitTest(unittest.TestCase):
    TESTCASES_MIDDLE_OF_THE_LINKED_LIST = [
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
    ]
    TESTCASES_MIDDLE_OF_LINKED_LIST = [
        ([1, 2, 3], 2)
    ]

    def test_middle_of_the_linked_list(self):
        for input_ln, output_ln in self.TESTCASES_MIDDLE_OF_THE_LINKED_LIST:
            input_ln = ListNode.from_list(input_ln)
            self.assertEqual(output_ln, middle_of_the_linked_list(input_ln).to_list())

    def test_middle_of_linked_list(self):
        for nums, expected in self.TESTCASES_MIDDLE_OF_LINKED_LIST:
            list_node = ListNode.from_list(nums)
            self.assertEqual(expected, middle_of_linked_list(list_node).val)
