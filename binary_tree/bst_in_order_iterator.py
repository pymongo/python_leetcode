from .binary_tree import TreeNode
import unittest
import collections


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = collections.deque()
        self.curr_node = root
        while self.curr_node:
            self.stack.append(self.curr_node)
            self.curr_node = self.curr_node.left

    def next(self) -> int:
        node = self.stack.pop()
        self.curr_node = node.right
        while self.curr_node:
            self.stack.append(self.curr_node)
            self.curr_node = self.curr_node.left
        return node.val

    def has_next(self) -> bool:
        if self.stack:
            return True
        else:
            return False


class TestBSTIterator(unittest.TestCase):
    def test(self):
        root = TreeNode.from_str("7(3)(15(9)(20))")
        bst = BSTIterator(root)
        self.assertEqual(3, bst.next())
        self.assertEqual(7, bst.next())
        self.assertEqual(True, bst.has_next())
        self.assertEqual(9, bst.next())
        self.assertEqual(15, bst.next())
        self.assertEqual(20, bst.next())
        self.assertEqual(False, bst.has_next())
