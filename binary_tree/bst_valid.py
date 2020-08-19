from .binary_tree import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev_val = float('-inf')

        def is_not_bst(node: TreeNode):
            if node is None:
                return False
            if is_not_bst(node.left):
                return True
            if self.prev_val >= node.val:
                return True
            # 离开当前层递归时即将进入右子树递归时，更新上一层递归的节点的值(self.prev_val)
            self.prev_val = node.val
            if is_not_bst(node.right):
                return True
            return False

        return not is_not_bst(root)
