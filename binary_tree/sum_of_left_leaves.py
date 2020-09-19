from .binary_tree import TreeNode


class Solution:
    @staticmethod
    def helper(node: TreeNode, is_left: bool) -> int:
        if node.left is None and node.right is None:
            if is_left:
                return node.val
            else:
                return 0
        res = 0
        if node.right:
            res += Solution.helper(node.right, False)
        if node.left:
            res += Solution.helper(node.left, True)
        return res

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        if root:
            ans += self.helper(root, False)
        return ans
