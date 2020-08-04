import unittest
from typing import Optional, List


class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next: Optional[ListNode] = None


# 看过Rust源码就知道，HashSet其实就是value=()的HashMap
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # HashMap内部元素个数
        self.elements_count: int = 0
        # HashMap内部bucket数组的长度
        self.capacity: int = 16384
        # HashMap内部的数组, 用dummyHead的好处是Python没有显示指出引用修改，还是固定bucket数组，只修改数组各元素的next指针更好，不会出现UB
        # 缺点是初始化好慢啊，容易超时
        self.bucket: List[ListNode] = [ListNode(key=-1, value=0)] * self.capacity

    def put(self, key: int, value: int) -> None:
        if self.elements_count * 5 > self.capacity:
            self._rehashing(self.capacity * 2)
        index = key % self.capacity
        curr_node = self.bucket[index]
        while curr_node is not None:
            if curr_node.key == key:
                # If the key already exists in the HashMap, update the value
                curr_node.value = value
                return
            curr_node = curr_node.next

        new_node = ListNode(key, value)
        new_node.next = self.bucket[index].next
        self.bucket[index].next = new_node
        self.elements_count += 1

    def get(self, key: int) -> int:
        curr_node = self.bucket[key % self.capacity]
        while curr_node is not None:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next
        return -1

    def remove(self, key: int) -> None:
        bucket_index = key % self.capacity
        curr_node = self.bucket[bucket_index]
        last_node = curr_node
        while curr_node is not None:
            if curr_node.key == key:
                # Remove
                last_node.next = curr_node.next
                # del curr_node
                self.elements_count -= 1
                return
            last_node = curr_node
            curr_node = curr_node.next

    def contains(self, key: int) -> bool:
        curr_node = self.bucket[key % self.capacity]
        while curr_node is not None:
            if curr_node.key == key:
                return True
            curr_node = curr_node.next
        return False

    def _rehashing(self, new_capacity: int):
        new_bucket: List[ListNode] = [ListNode(key=-1, value=0)] * self.capacity * new_capacity
        for node in self.bucket:
            curr_node = node
            while curr_node is not None:
                curr_new_bucket_node = new_bucket[curr_node.key % new_capacity]
                new_bucket_node = ListNode(curr_node.key, curr_node.value)
                new_bucket_node.next = curr_new_bucket_node.next
                curr_new_bucket_node.next = new_bucket_node

                curr_node = curr_node.next
        self.bucket = new_bucket
        self.capacity = new_capacity


class Testing(unittest.TestCase):
    def test_remove(self):
        m = MyHashMap()
        m.put(1, 1)
        m.put(129, 129)
        m.put(257, 257)
        # 257->129->1

        m.remove(129)
        # 257->1
        self.assertEqual(257, m.get(257))
        self.assertEqual(-1, m.get(129))
        self.assertEqual(1, m.get(1))
        m.remove(1)
        self.assertEqual(257, m.get(257))
        self.assertEqual(-1, m.get(129))
        self.assertEqual(-1, m.get(1))
        m.remove(257)
        self.assertEqual(-1, m.get(257))
        self.assertEqual(-1, m.get(129))
        self.assertEqual(-1, m.get(1))
        m.put(129, 129)
        m.put(1, 1)
        self.assertEqual(-1, m.get(257))
        self.assertEqual(129, m.get(129))
        self.assertEqual(1, m.get(1))
        m.remove(257)
        self.assertEqual(-1, m.get(257))
        self.assertEqual(129, m.get(129))
        self.assertEqual(1, m.get(1))
        m.remove(129)
        self.assertEqual(-1, m.get(257))
        self.assertEqual(-1, m.get(129))
        self.assertEqual(1, m.get(1))

    def test_my_hash_map(self):
        my_map = MyHashMap()
        my_map.put(1, 1)
        my_map.put(2, 2)
        self.assertEqual(1, my_map.get(1))
        self.assertEqual(-1, my_map.get(3))
        my_map.put(2, 1)
        self.assertEqual(1, my_map.get(2))
        my_map.remove(2)
        self.assertEqual(-1, my_map.get(2))

        my_map.put(16, 1)
