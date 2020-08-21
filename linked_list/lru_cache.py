"""
# 如何理解: 最近的最少使用次数
错误理解: 通过HashMap记录每个num的get调用次数，反例: 如果每个num都被调用了1次，要取哪一个？
正确理解: 不仅要考虑调用次数，还要从时间的角度去考虑(最近)
维护一条链表，新的元素都加到链表尾部，这样头部的元素最旧，尾部的元素是最新元素
如果某个节点被访问了一次，则将该节点移到链表尾部(标记为最新)
这样下次来新的节点时，要删老的节点，就只会删头部的节点了
"""
import unittest
import collections
from typing import Dict, Optional


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


# 这是我多次修改，代码量少可读性强的LRU版本，面试时默写这个就够了
class MyBestLRU:

    def __init__(self, capacity: int):
        self.len = 0
        self.max_size = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = dict()

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        node = self.m[key]
        self._move_back(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            node = self.m[key]
            node.value = value
            self._move_back(node)
            return
        if self.len == self.max_size:
            first_node = self.head.next
            self.m.pop(first_node.key)

            first_node.next.prev = self.head
            self.head.next = first_node.next

        node = Node(key, value)
        self.m[key] = node
        self._move_back(node)

        if self.len < self.max_size:
            self.len += 1

    def _move_back(self, node: Node):
        node_prev = node.prev
        node_next = node.next
        if node_prev and node_next:
            # 如果不是新创建的节点，则需要将剥离节点的前后节点互连
            node_prev.next = node_next
            node_next.prev = node_prev

        tail_prev = self.tail.prev

        # 2. 将剥离出来/新生成的节点插入到末尾
        tail_prev.next = node
        node.prev = tail_prev

        node.next = self.tail
        self.tail.prev = node


class ListNode:
    def __init__(self, key: int, value: int):
        # value will always be positive
        self.key: int = key
        self.value: int = value
        self.prev: Optional[ListNode] = None
        self.next: Optional[ListNode] = None

    # def __repr__(self):
    #     s = ""
    #     curr = self
    #     while curr:
    #         s += str(curr.key)
    #         s += "->"
    #         curr = curr.next
    #     return s[:-2]


# 用处: 内存淘汰算法，哪些数据访问次数少/比较旧，就把它扔掉
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.elements_count: int = 0
        self.is_full: bool = False
        # dummy head and dummy tail
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        # HashMap<key, ListNode>
        self.node_map: Dict[int, ListNode] = dict()

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._move_node_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            # 如果key已存在，则更新相应的value，并将节点挪到链表尾巴
            update_node = self.node_map[key]
            update_node.value = value
            self._move_node_to_tail(update_node)
            return

        if self.is_full:
            # 链表头部删掉一个节点
            remove_node = self.head.next
            self.node_map.pop(remove_node.key)
            remove_node.next.prev = self.head
            self.head.next = remove_node.next

        new_node = ListNode(key, value)

        # TODO 如果用单链表+prev_map，这里维护prev_map很恶心，代码容易乱
        # new_node与self.tail.prev互连
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node

        # new_node与self.tail互连
        self.tail.prev = new_node
        new_node.next = self.tail

        self.node_map[key] = new_node
        if not self.is_full:
            self.elements_count += 1
            if self.elements_count == self.capacity:
                self.is_full = True

    # 做链表类题，最好用图画出每个函数输入输出对链表的变化，这样才不容易乱
    # Change: head->...->node->...->tail
    # To    : head->...->node->tail
    def _move_node_to_tail(self, node: ListNode):
        if node.next == self.tail:
            # 如果节点已经是最后一个节点了，就不需要挪动了
            return

        # 从链表中剪掉update_node
        node.prev.next = node.next
        node.next.prev = node.prev

        # 将update_node与self.tail.prev建立连接
        self.tail.prev.next = node
        node.prev = self.tail.prev

        # 将update_node与self.tail建立连接
        node.next = self.tail
        self.tail.prev = node
        return


class UseOrderedDict(collections.OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity: int = capacity
        self.elements_count: int = 0
        self.is_full: bool = False
        # remembers the order entries were added

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def set(self, key: int, value: int):
        if key in self:
            self.move_to_end(key)
            self[key] = value
            return
        if self.is_full:
            # pop first item
            self.popitem(last=False)
            self[key] = value
        else:
            self[key] = value
            self.elements_count += 1
            if self.elements_count == self.capacity:
                self.is_full = True


class Testing(unittest.TestCase):
    def test_put_insert_or_update(self):
        lru = LRUCache(1)
        lru.put(1, 1)
        self.assertEqual(1, lru.get(1))
        lru.put(1, 2)
        self.assertEqual(2, lru.get(1))

    def test_remove_head(self):
        lru = LRUCache(1)
        lru.put(1, 1)
        self.assertEqual(1, lru.get(1))
        lru.put(2, 2)
        self.assertEqual(-1, lru.get(1))
        self.assertEqual(2, lru.get(2))

    def test_lru(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)

        self.assertEqual(1, lru.get(1))
        # lru.get(1)

        lru.put(3, 3)  # evicts key 2(会覆盖掉2，因为1之前被读取过，会挪到尾部)

        self.assertEqual(-1, lru.get(2))
        # lru.get(2)

        lru.put(4, 4)  # evicts key 1

        # lru.get(1)
        self.assertEqual(-1, lru.get(1))

        self.assertEqual(3, lru.get(3))
        self.assertEqual(4, lru.get(4))
