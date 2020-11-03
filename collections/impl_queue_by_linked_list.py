"""
[lintcode only](https://www.lintcode.com/problem/implement-queue-by-linked-list/)
两种主要的队列
1. TODO PriorityQueue: 基于堆实现，非FIFO(最先出队的是优先级高的元素)
2. 普通Queue: 基于链表或数组(循环队列)实现
"""
import unittest


class MyListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        list_node = MyListNode(item)
        if self.rear is None:
            self.front = list_node
            self.rear = list_node
        else:
            self.rear.next = list_node
            self.rear = list_node

    def dequeue(self):
        if self.front is None:
            return None
        result = self.front.val
        # 没必要的分支判断
        # if self.front == self.rear:
        #     self.front = None
        #     self.rear = None
        # else:
        self.front = self.front.next
        return result


class TestMyQueue(unittest.TestCase):
    TESTCASES = [
        ([1, 2, 3], [1, 2]),
        ([10], [10])
    ]

    def test_my_queue(self):
        for enqueues, dequeues in self.TESTCASES:
            queue = MyQueue()
            for number in enqueues:
                queue.enqueue(number)
            for each in dequeues:
                self.assertEqual(each, queue.dequeue())
