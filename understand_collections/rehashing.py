"""
rehashing(哈希扩容)，发现哈希冲突严重容量不够用之后，基本用倍增法将capacity(容量)翻倍
"""
import unittest
from list_node.list_node import ListNode
from typing import List, Optional


# 这题是元素个数超过1/10 capacity就倍增扩容，实际上Java里更多是30%-40%就kor
# FIXME 负数MOD问题: Python/Ruby: -1%3 = 2, Java/Rust: -1%3 = -1
# FIXME JAVA/Rust负数%要用 (-1%3 + 3) % 3 = 2
def rehashing(hash_table: List[Optional[ListNode]]) -> List[Optional[ListNode]]:
    nums: List[int] = []
    old_capacity = 0
    elements_count = 0
    for each in hash_table:
        old_capacity += 1
        if each is None:
            continue
        curr_node = each
        while curr_node is not None:
            elements_count += 1
            # nums.append(curr_node.val)
            # 本题要求按栈的顺序遍历旧哈希表的数据，实际上顺序是无所谓的
            nums.insert(0, curr_node.val)
            curr_node = curr_node.next
    # print(elements_count, old_capacity, nums)
    if elements_count * 10 < old_capacity:
        return hash_table
    new_capacity = old_capacity * 2
    new_hash_table: List[Optional[ListNode]] = [None] * new_capacity
    for num in nums:
        new_index = num % new_capacity
        if new_hash_table[new_index] is None:
            new_hash_table[new_index] = ListNode(num)
        else:
            new_node = ListNode(num)
            new_node.next = new_hash_table[new_index]
            new_hash_table[new_index] = new_node
    return new_hash_table


class Testing(unittest.TestCase):
    TEST_CASES = [
        (['', '', '29->5'], ['', '', '', '', '', '29->5']),
        (['', '21->9', '14', ''], ['', '9', '', '', '', '21', '14', '']),
    ]

    def test_rehashing(self):
        for input_list_str, expected_list_str in self.TEST_CASES:
            input_hash_table = [ListNode.from_str(s) for s in input_list_str]
            output_hash_table = rehashing(input_hash_table)
            output_list_str = ["" if node is None else str(node) for node in output_hash_table]
            self.assertListEqual(expected_list_str, output_list_str)
