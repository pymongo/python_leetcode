from .binary_tree import TreeNode


# 将一颗BST每个节点的值改为大于等于该节点值的所有值之和
class Solution:
    @staticmethod
    def bst_to_gst(root: TreeNode) -> TreeNode:
        _sum = 0

        def helper(node: TreeNode):
            nonlocal _sum
            if node is None:
                return
            helper(node.right)
            _sum += node.val
            node.val = _sum
            helper(node.left)

        helper(root)
        return root
