import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next_node=None):
        self.val: int = val
        self.next: Optional[ListNode] = next_node

    # ListNode{val: 4, next: ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: None}}}}
    def __str__(self) -> str:
        return f'ListNode{{val: {self.val}, next: {"None" if self.next is None else self.next.__str__()}}}'

    def __repr__(self) -> str:
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
            curr_node = curr_node.next
            nums.append(curr_node.val)
        return nums

    @staticmethod
    def from_list(nums: List[int]) -> Optional['ListNode']:
        if not nums:
            return None
        dummy_head = ListNode(-1)
        curr_node = dummy_head
        for num in nums:
            curr_node.next = ListNode(num)
            curr_node = curr_node.next
        return dummy_head.next

    @staticmethod
    def from_str(s: str) -> Optional['ListNode']:
        if not s:
            return None
        nums = [int(num) for num in s.split("->")]
        return ListNode.from_list(nums)


# Private Class
class _TestListNode(unittest.TestCase):
    def test_from_list(self):
        list_node = ListNode.from_list([1, 2])
        self.assertEqual(1, list_node.val)
        self.assertEqual(2, list_node.next.val)

    def test_to_list(self):
        nums1 = [1, 2, 3]
        list_node = ListNode.from_list(nums1)
        print(list_node)
        nums2 = list_node.to_list()
        self.assertEqual(nums1, nums2)

    def test_to_string(self):
        list_node = ListNode.from_list([1, 2, 3])
        self.assertEqual("1->2->3", str(list_node))

if __name__ == '__main__':
    node = ListNode.from_list([4,2,1,3])
    print(node)
    assert node.__str__() == r"ListNode{val: 4, next: ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 3, next: None}}}}"
