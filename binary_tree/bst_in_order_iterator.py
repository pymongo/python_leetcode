"""
终极方案: 莫里斯遍历(Morris)+线索二叉树(threaded_binary_tree)
关键词: successor, predecessor
在遍历的时候，利用predecessor的右空指针，将其指向当前节点

"""
from .binary_tree import TreeNode
import unittest
import collections


# BST中最小的节点是从根节点一直往左走遇见的叶子节点，它不一定在树的最底层
# 如果BST是一个平衡二叉树(满二叉树)，查找最小值的耗时是O(logn)，否则是O(n) (一条链)
class BSTIterator:

    # 另一种笨方法是初始化时直接生成中序数组，然后next去取，但是不满足O(h),h为二叉树最大高度的空间复杂度
    # 因为stack保存的是一条路径上的节点，所以stack的空间复杂度是O(h)
    def __init__(self, root: TreeNode):
        # 根节点到左叶子节点上路径的节点，stack还表示右子树还没访问过的节点
        self.stack = collections.deque()
        self.curr_node = root
        while self.curr_node:
            self.stack.append(self.curr_node)
            self.curr_node = self.curr_node.left

    # 这题=中序遍历迭代版的代码
    def next(self) -> int:
        node = self.stack.pop()
        self.curr_node = node.right
        # 如果有右子树，则右子树入栈直到最底的左节点
        # 如果没有右子树，下次调用next()时弹出的就是node的父节点，现在的node下次弹出的node的左儿子
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
