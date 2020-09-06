from binary_tree.binary_tree import TreeNode


class Solution:
    @staticmethod
    def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = []
        stack.append(cloned)
        target_val = target.val
        while stack:
            node = stack.pop()
            if node.val == target_val:
                return node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
