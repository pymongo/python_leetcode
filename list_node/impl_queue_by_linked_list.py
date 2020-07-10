"""
[lintcode only](https://www.lintcode.com/problem/implement-queue-by-linked-list/)
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
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        return result


class TestMyQueue(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3], [3, 2]),
        ([10], [10])
    ]

    def test_my_queue(self):
        for enqueues, dequeues in self.TEST_CASES:
            queue = MyQueue()
            for number in enqueues:
                queue.enqueue(number)
            for each in dequeues:
                self.assertEqual(each, queue.dequeue())
            self.assertEqual(1, 2)
