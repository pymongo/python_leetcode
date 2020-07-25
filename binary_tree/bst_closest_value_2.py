import unittest
from .binary_tree import TreeNode
from typing import List
import collections


# 我的思路: 先找到中序遍历的数组，然后根据有序数组最接近目标值的k项这题的二分法进行数据筛选
def bst_closest_1(root: TreeNode, target: float, k: int) -> List[int]:
    result = []
    if root is None:
        return result
    in_order = []
    size = 0
    stack = collections.deque()
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        node = stack.pop()
        in_order.append(node.val)
        size += 1
        curr = node.right

    # 第二部分，在中序遍历的有序数组中查找与target最接近的k项，参考[Find K Closest Elements]这题
    start, end = 0, size-k+1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if target - in_order[mid] > in_order[mid+k-1] - target:
            start = mid
        else:
            end = mid
    return in_order[start:start+k]


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("3(1()(2))(4)", 0.275000, 2, [1, 2]),
        ("2(1)(3)", 5.571429, 2, [2, 3]),
    ]

    def test_bst_closest_1(self):
        for binary_tree, target, k, expected in self.TEST_CASES:
            root = TreeNode.from_str(binary_tree)
            print(root)
            self.assertEqual(expected, bst_closest_1(root, target, k))
