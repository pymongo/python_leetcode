import unittest
from typing import List


class ListNode:
    def __init__(self, num):
        self.val: int = num
        self.next = None

    def __str__(self) -> str:
        list_node_to_string: str = str(self.val)
        curr_node = self
        while curr_node.next is not None:
            curr_node = curr_node.next
            list_node_to_string += f"->{curr_node.val}"
        return list_node_to_string

    def to_list(self) -> List[int]:
        nums = [self.val]
        curr_node = self
        while curr_node.next is not None:
            nums.append(curr_node.val)
            curr_node = curr_node.next
        return nums

    @staticmethod
    def from_list(nums: List[int]):
        dummy_head = ListNode(-1)
        curr_node = dummy_head
        for num in nums:
            curr_node.next = ListNode(num)
            curr_node = curr_node.next
        return dummy_head.next


# Private Class
class _TestListNode(unittest.TestCase):
    def test_from_list(self):
        list_node = ListNode.from_list([1, 2])
        self.assertEqual(1, list_node.val)
        self.assertEqual(2, list_node.next.val)

    def test_to_string(self):
        list_node = ListNode.from_list([1, 2, 3])
        self.assertEqual("1->2->3", str(list_node))
