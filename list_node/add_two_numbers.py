from .list_node import ListNode
import unittest


# 在所有 Python3 提交中击败了 99.82% 的用户
def add_two_numbers(ln1: ListNode, ln2: ListNode) -> ListNode:
    dummy_head = ListNode(-1)
    curr_node = dummy_head
    sum_or_carry = 0
    while True:
        if ln1 is None and ln2 is None:
            break
        elif ln1 is None and ln2 is not None:
            sum_or_carry = sum_or_carry + ln2.val
            curr_node.next = ListNode(sum_or_carry % 10)
            curr_node = curr_node.next
            sum_or_carry //= 10
            ln2 = ln2.next
        elif ln1 is not None and ln2 is None:
            sum_or_carry = sum_or_carry + ln1.val
            curr_node.next = ListNode(sum_or_carry % 10)
            curr_node = curr_node.next
            sum_or_carry //= 10
            ln1 = ln1.next
        else:
            sum_or_carry = sum_or_carry + ln1.val + ln2.val
            curr_node.next = ListNode(sum_or_carry % 10)
            curr_node = curr_node.next
            sum_or_carry //= 10
            ln1 = ln1.next
            ln2 = ln2.next
    if sum_or_carry > 0:
        curr_node.next = ListNode(sum_or_carry)
        curr_node = curr_node.next
    return dummy_head.next


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([5], [5], [0, 1])
    ]

    def test_add_two_numbers(self):
        for ln1, ln2, expected in self.TEST_CASES:
            ln1 = ListNode.from_list(ln1)
            ln2 = ListNode.from_list(ln2)
            self.assertEqual(expected, add_two_numbers(ln1, ln2).to_list())
