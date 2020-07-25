import unittest
from .binary_tree import TreeNode
from typing import List
import collections


# 我的思路: 先找到中序遍历的数组，然后根据有序数组最接近目标值的k项这题的二分法进行数据筛选
# 其它思路: 将对BST的操作抽象成对一位数组的操作，move_upper和move_lower是镜像操作，left 和 right 互相换一下就行。 相当于在 bst 里get next node & get previous node
# 我的思路背下来后可以同时解决迭代中序遍历+[Find K Closest Elements]两题
def bst_closest_1(root: TreeNode, target: float, k: int) -> List[int]:
    in_order = []
    if root is None:
        return in_order
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
    start, end = 0, size - k
    while start < end:
        mid = start + (end - start) // 2
        if target - in_order[mid] > in_order[mid + k] - target:
            start = mid + 1
        else:
            end = mid
    return in_order[start:start + k]


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
