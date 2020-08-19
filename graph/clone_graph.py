import unittest
import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def my_bfs(node: Node):
    if not node:
        return None
    # key: old_node, value: new_node(same val to old_node)
    old_new_mapping = dict()
    new_node_root = Node(node.val)
    old_new_mapping[node] = new_node_root

    q = collections.deque()
    q.append(node)
    while q:
        temp_node = q.popleft()
        for neighbor in temp_node.neighbors:
            if neighbor not in old_new_mapping:
                old_new_mapping[neighbor] = Node(neighbor.val)
                q.append(neighbor)
            old_new_mapping[temp_node].neighbors.append(old_new_mapping[neighbor])
    return new_node_root


# 这样做其实不太好，一边遍历一边复制，没法拆分代码
# 参考复制链表一题，更好的思路是: 先复制所有点，再复制所有点的邻居(边的关系)
def my_dfs_entrance(node: Node) -> Node:
    # key: old_node, value: new_node(same val to old_node)
    old_new_mapping = dict()
    return my_dfs(node, old_new_mapping)


def my_dfs(node: Node, old_new_mapping):
    if node is None:
        return
    if node in old_new_mapping:
        return old_new_mapping[node]
    # lintcode上用clone_node = UndirectedGraphNode(node.label)
    cloned_node = Node(node.val)
    old_new_mapping[node] = cloned_node
    for neighbor in node.neighbors:
        cloned_node.neighbors.append(my_dfs(neighbor, old_new_mapping))
    return cloned_node


def generate_test_case() -> Node:
    # 1,2,3,4逆时针围成一个圈
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_1.neighbors = [node_2, node_4]
    node_2.neighbors = [node_1, node_3]
    node_3.neighbors = [node_2, node_4]
    node_4.neighbors = [node_1, node_3]
    return node_1


class Testing(unittest.TestCase):
    def test_my_dfs(self):
        node = generate_test_case()
        new_node = my_dfs_entrance(node)
        self.assertNotEqual(hash(node), hash(new_node))
