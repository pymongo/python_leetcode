from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder_recursive(root: Node) -> List[int]:
    res = []

    def dfs(node: 'Node'):
        if node is None:
            return
        res.append(node.val)
        for child in node.children:
            dfs(child)

    dfs(root)
    return res


def preorder_iterative(root: Node) -> List[int]:
    if root is None:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        res.append(node.val)
        # 因为栈是FILO的，但是希望靠左的儿子能优先被遍历，所以只好将儿子反转
        for child in reversed(node.children):
            stack.append(child)
    return res


def postorder_recursive(root: Node) -> List[int]:
    res = []

    def dfs(node: 'Node'):
        if node is None:
            return
        for child in node.children:
            dfs(child)
        res.append(node.val)

    dfs(root)
    return res
