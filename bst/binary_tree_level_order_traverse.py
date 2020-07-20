"""
这题输入用例是二叉树，需要构思一种创建二叉树的方式才能构建单元测试
TODO 先不写单元测试，等leetcode做到pretty print二叉树以及创建二叉树的相关题目时再补充单元测试
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


import collections


# 那么二叉树的经典遍历pre-order, in-order, after-order就只能用递归吗?
def binary_tree_level_order(root: TreeNode):
    if not root:
        return []
    # Queue内部有锁，性能不如deque
    # deque实际上是双向队列(可以从左边或右边入队/出队)，但是我们当做单向队列用
    q = collections.deque([root])
    result = []
    # 队列不为空时
    while q:
        current_level_values = []
        # 每次都要重新去队列长度
        for i in range(len(q)):
            node = q.popleft()
            current_level_values.append(node.val)
            # 将遍历当层二叉树节点的所有子树移到队尾，留给下一轮遍历
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(current_level_values)
    return result
