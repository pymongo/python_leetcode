from .binary_tree import TreeNode


class Solution:
    def recursive_accepted(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        中序遍历，找到两对非有序的节点，最后交换它们
        如何在找到第二个节点后，直接退出循环？
        """
        # 需要互换位置的，两个错误的节点
        self.first, self.second = None, None
        # 存储上一层递归的前继
        # noinspection PyTypeChecker
        self.prev = TreeNode(float("-inf"))

        def in_order_check(node: TreeNode):
            if node is None:
                return

            in_order_check(node.left)
            # 为什么一定是第一次的前一个节点和第二次的后一个节点？
            # 假设bst原先的中序遍历是[1,2,3,4,5]
            # 然后2和4互换，中序遍历[1,4,3,2,5]，发现第一个错误在4>3，左边的交换过的，第二个错误在3>2，取右边的交换过的
            # FIXME 注意判断符是大于等于，因为两个节点值相等时就不是BST了(参考98题验证BST的规则)
            if self.first is None and self.prev.val >= node.val:
                # FIXME 不能在找到第一个错误值时，错误的认为相邻的两个节点都是错误的
                # self.first, self.second = self.prev, node
                self.first = self.prev
            if self.first and self.prev.val >= node.val:
                # 虽然初始化first时，second会设置成相邻的点，但是随着遍历
                self.second = node

            # 离开当前层递归时即将进入右子树递归时，更新全局的存储上一层递归的前继节点的指针
            self.prev = node
            in_order_check(node.right)

        in_order_check(root)
        # lintcode有一个测试用例是没有错误节点，所以lintcode版本要改成 if self.first and self.right
        assert self.first is not None
        assert self.second is not None
        self.first.val, self.second.val = self.second.val, self.first.val
