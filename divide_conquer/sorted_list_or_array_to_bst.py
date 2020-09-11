from linked_list.list_node import ListNode
from binary_tree.binary_tree import TreeNode
from typing import List


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # [left, right)
        def build_tree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            fast, slow = left, left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            root = TreeNode(slow.val)
            root.left = build_tree(left, slow)
            root.right = build_tree(slow.next, right)
            return root

        return build_tree(head, None)

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # left..=right
        def build_tree(left: int, right: int) -> TreeNode:
            # 注意如果右边界也选中的话，递归结束条件会略有不同
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = build_tree(left, mid - 1)
            root.right = build_tree(mid + 1, right)
            return root

        return build_tree(0, len(nums) - 1)
