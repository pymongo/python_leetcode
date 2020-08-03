import unittest
from typing import Optional, List


class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: Optional[ListNode] = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # HashMap内部元素个数
        self.elements_count: int = 0
        # HashMap内部bucket数组的长度
        self.capacity: int = 8
        # HashMap内部的数组
        self.bucket: List[Optional[ListNode]] = [None] * 8

    def put(self, key: int, value: int) -> None:
        # 如果key大于bucket的长度，容易出现哈希冲突
        if key > self.capacity:
            self._rehashing(key + 1)
        bucket_index: int = key % self.capacity
        if self.bucket[bucket_index] is None:
            if (self.elements_count + 1) * 2 > self.capacity:
                self._rehashing(self.capacity * 2)
            self.bucket[bucket_index] = ListNode(value)
            self.elements_count += 1
        else:
            # If the key already exists in the HashMap, update the value
            self.bucket[bucket_index].val = value

    def get(self, key: int) -> int:
        bucket_index = key % self.capacity
        if self.bucket[bucket_index] is None:
            return -1
        return self.bucket[bucket_index].val

    def remove(self, key: int) -> None:
        bucket_index = key % self.capacity
        if self.bucket[bucket_index] is None:
            return
        self.bucket[bucket_index] = None
        self.elements_count -= 1

    def contains(self, key: int) -> bool:
        return self.bucket[key % self.capacity] is None

    def _rehashing(self, new_capacity: int):
        for _ in range(new_capacity - self.capacity):
            self.bucket.append(None)
        self.capacity = new_capacity


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
hashMap.put(2, 1);          // update the existing value

hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 
"""

"""
["MyHashMap","put","put","put","remove","get","put","put","get","put","put","put","put","put","put","put","put","put","put","put","put","remove","put","remove","put","put","remove","put","get","put","get","put","put","put","put","put","get","put","remove","put","remove","put","put","put","put","put","remove","put","put","remove","put","put","put","get","get","put","remove","put","put","put","get","put","put","put","remove","put","put","put","put","put","get","put","put","get","get","put","remove","remove","get","put","remove","put","remove","put","put","put","get","put","put","put","remove","put","put","get","put","put","get","remove","get","get","put"]
[[],[24,31],[58,35],[59,88],[84],[62],[2,22],[44,70],[24],[24,42],[58,99],[74,29],[40,66],[55,83],[21,27],[31,25],[78,19],[86,70],[71,73],[39,95],[6,96],[76],[62,22],[78],[53,51],[66,53],[44],[14,46],[77],[15,32],[22],[53,79],[35,21],[73,57],[18,67],[96,61],[73],[58,77],[6],[5,58],[17],[25,14],[16,13],[4,37],[47,43],[14,79],[35],[7,13],[78,85],[27],[73,33],[95,87],[31,21],[20],[64],[90,22],[16],[77,50],[55,41],[33,62],[44],[73,16],[13,54],[41,5],[71],[81,6],[20,98],[35,64],[15,35],[74,31],[90],[32,15],[44,79],[37],[53],[22,80],[24],[10],[7],[53,61],[65],[63,99],[47],[97,68],[7,0],[9,25],[97],[93,13],[92,43],[83,73],[74],[41,78],[39,28],[52],[34,16],[93,63],[82],[77],[16],[50],[68,47]]
[null,null,null,null,null,-1,null,null,-1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,90,null,-1,null,null,40,null,null,null,null,null,29,null,null,null,null,17,null,null,null,null,null,null,null,null,null,33,null,null,null,null,null,null,18,null,null,-1,null,null,-1,35,null,null,null,null,null,null,null,-1,-1,null,null,null,null,null,-1,null,null,null,null,null,null,null,null,null,null,null,null,null,-1,null,null,null,null,87,null,null]
[null,null,null,null,null,-1,null,null,-1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,90,null,50,null,null,40,null,null,null,null,null,29,null,null,null,null,17,null,null,null,null,null,null,null,null,null,33,null,null,null,null,null,null,18,null,null,-1,null,null,-1,35,null,null,null,null,null,null,null,-1,-1,null,null,null,null,null,-1,null,null,null,null,null,null,null,null,null,null,null,null,null,-1,null,null,null,null,87,null,null]
"""

"""
[None,None,None,None,None,-1,None,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,90,None,50,None,None,40,None,None,None,None,None,29,None,None,None,None,17,None,None,None,None,None,None,None,None,None,33,None,None,None,None,None,None,18,None,None,-1,None,None,-1,35,None,None,None,None,None,None,None,-1,-1,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,None,-1,None,None,None,None,87,None,None]

"""


class Testing(unittest.TestCase):
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

    def test_my_hash_map_2(self):
        m = MyHashMap()
        operations = ["put", "put", "put", "remove", "get", "put", "put", "get", "put", "put", "put", "put", "put",
                      "put", "put", "put", "put", "put", "put", "put", "remove", "put", "remove", "put", "put",
                      "remove",
                      "put",
                      "get", "put", "get", "put", "put", "put", "put", "put", "get", "put", "remove", "put", "remove",
                      "put",
                      "put", "put", "put", "put", "remove", "put", "put", "remove", "put", "put", "put", "get", "get",
                      "put",
                      "remove", "put", "put", "put", "get", "put", "put", "put", "remove", "put", "put", "put", "put",
                      "put",
                      "get", "put", "put", "get", "get", "put", "remove", "remove", "get", "put", "remove", "put",
                      "remove",
                      "put", "put", "put", "get", "put", "put", "put", "remove", "put", "put", "get", "put", "put",
                      "get",
                      "remove", "get", "get", "put"]
        data = [[24, 31], [58, 35], [59, 88], [84], [62], [2, 22], [44, 70], [24], [24, 42], [58, 99], [74, 29],
                [40, 66], [55, 83], [21, 27], [31, 25], [78, 19], [86, 70], [71, 73], [39, 95], [6, 96], [76],
                [62, 22], [78], [53, 51], [66, 53], [44], [14, 46], [77], [15, 32], [22], [53, 79], [35, 21], [73, 57],
                [18, 67], [96, 61], [73], [58, 77], [6], [5, 58], [17], [25, 14], [16, 13], [4, 37], [47, 43],
                [14, 79], [35], [7, 13], [78, 85], [27], [73, 33], [95, 87], [31, 21], [20], [64], [90, 22], [16],
                [77, 50], [55, 41], [33, 62], [44], [73, 16], [13, 54], [41, 5], [71], [81, 6], [20, 98], [35, 64],
                [15, 35], [74, 31], [90], [32, 15], [44, 79], [37], [53], [22, 80], [24], [10], [7], [53, 61], [65],
                [63, 99], [47], [97, 68], [7, 0], [9, 25], [97], [93, 13], [92, 43], [83, 73], [74], [41, 78],
                [39, 28], [52], [34, 16], [93, 63], [82], [77], [16], [50], [68, 47]]
        expected = [None, None, None, None, -1, None, None, -1, None, None, None, None, None, None, None, None, None,
                    None, None, None, None, None, None, 90, None, 50, None, None, 40, None, None, None, None, None, 29,
                    None, None, None, None, 17, None, None, None, None, None, None, None, None, None, 33, None, None,
                    None, None, None, None, 18, None, None, -1, None, None, -1, 35, None, None, None, None, None, None,
                    None, -1, -1, None, None, None, None, None, -1, None, None, None, None, None, None, None, None,
                    None, None, None, None, None, -1, None, None, None, None, 87, None, None]
        for i in range(len(operations)):
            print(operations[i], str(data[i]).replace('[', '(').replace(']', ')'), f" expected: {expected[i]}", sep='')
            if len(data[i]) == 1:
                if operations[i] == 'get':
                    self.assertEqual(expected[i], m.get(data[i][0]))
                elif operations[i] == 'remove':
                    self.assertEqual(expected[i], m.remove(data[i][0]))
            elif len(data[i]) == 2:
                self.assertEqual(expected[i], m.put(data[i][0], data[i][1]))
            else:
                raise Exception("Unreachable")

"""
[null,null,null,null,null,-1,null,null,-1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,90,null,-1,null,null,40,null,null,null,null,null,29,null,null,null,null,17,null,null,null,null,null,null,null,null,null,33,null,null,null,null,null,null,-1,null,null,-1,null,null,-1,35,null,null,null,null,null,null,null,-1,-1,null,null,null,null,null,-1,null,null,null,null,null,null,null,null,null,null,null,null,null,-1,null,null,null,null,87,null,null]



[null,null,null,null,null,-1,null,null,-1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,90,null,-1,null,null,40,null,null,null,null,null,29,null,null,null,null,17,null,null,null,null,null,null,null,null,null,33,null,null,null,null,null,null,18,null,null,-1,null,null,-1,35,null,null,null,null,null,null,null,-1,-1,null,null,null,null,null,-1,null,null,null,null,null,null,null,null,null,null,null,null,null,-1,null,null,null,null,87,null,null]
"""
