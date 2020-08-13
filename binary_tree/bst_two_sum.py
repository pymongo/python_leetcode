from .binary_tree import TreeNode


class Solution:
    @staticmethod
    def is_target_two_sum_in_bst(root: TreeNode, target: int) -> bool:
        visited = set()

        def search(node: TreeNode) -> bool:
            if node is None:
                return False
            # pre_order
            if target - node.val in visited:
                return True
            visited.add(node.val)
            return search(node.left) or search(node.right)

        return search(root)

    @staticmethod
    def find_a_two_sum_pair(root: TreeNode, target: int):
        visited = dict()

        def search(node: TreeNode):
            if node is None:
                return None
            # pre_order
            if node.val in visited:
                return [visited[node.val], node.val]
            visited[target - node.val] = node.val
            left_res = search(node.left)
            if left_res:
                return left_res
            right_res = search(node.right)
            if right_res:
                return right_res

        return search(root)


class BSTTwoSumO1Space:
    class Solution:
        """
        @param: : the root of tree
        @param: : the target sum
        @return: two numbers from tree which sum is n
        """

        def twoSum(self, root, n):
            # write your code here
            if not root:
                return

            min_node = self.get_min_node(root)
            max_node = self.get_max_node(root)
            left_node, right_node = min_node, max_node

            while left_node != right_node:
                pivot = left_node.val + right_node.val
                if pivot == n:
                    return [left_node.val, right_node.val]
                elif pivot < n:
                    left_node = self.get_successor_node(root, left_node)
                else:
                    right_node = self.get_predecessor_node(root, right_node)

            return

        def get_min_node(self, root):
            node = root
            while node.left:
                node = node.left
            return node

        def get_max_node(self, root):
            node = root
            while node.right:
                node = node.right
            return node

        def get_successor_node(self, root, p):
            node, upper = root, None
            while node:
                if node.val > p.val:
                    upper = node
                    node = node.left
                else:
                    node = node.right
            return upper

        def get_predecessor_node(self, root, p):
            node, lower = root, None
            while node:
                if node.val < p.val:
                    lower = node
                    node = node.right
                else:
                    node = node.left
            return lower
