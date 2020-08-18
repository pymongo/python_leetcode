import unittest
from .list_node import ListNode
from typing import Optional


# 这道题面试要求O(1)空间复杂度，所以不能像first_unique_number这题一样用HashMap记录链表节点
class Solution(unittest.TestCase):
    @staticmethod
    def is_cycle(head: ListNode) -> bool:
        """
        小学的操场追击问题: 只有链表内有环，快指针一定能追上慢指针
        """
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def test_find_cycle_intersect(self):
        head = ListNode(1)

        second = ListNode(2)
        head.next = second

        third = ListNode(3)
        second.next = third

        fourth = ListNode(4)
        third.next = fourth

        fourth.next = second
        print(self.find_cycle_intersect(head).val)

    @staticmethod
    def find_cycle_intersect(head: ListNode) -> Optional[ListNode]:
        """
        TODO Floyd算法、Floyd判圈算法(龟兔赛跑算法)
        Floyd 的算法被划分成两个不同的 阶段(Phase):
        第一个阶段(追击问题)去判断图中是否存在环
        第二个阶段(相遇问题)慢指针继续走，另一根指针从起点出发，如果相遇则相遇点一定是环的入口
        如图，快慢指针相遇的节点时环中右下节点
        起点到环入口 的路径长度为 a
        环入口到相遇点 的路径长度为 b
        相遇点到环入口 的路径长度为 c
        快慢指针在环内相遇，那么快指针已经走了一圈了，所以快指针走过的路径是 a + b + c + b
        快指针走过的路径=慢指针的两倍
        a+b+c+b = 2(a+b)
        所以a=c，也就相遇点到环的路径长度等于入口到相遇点的路径长度
        o->o->o->o
              ↑  ↓
              o← o
        Floyd判圈/龟兔赛跑法除了能解决链表/图，还能解决leetcode_202(happy number)这样，某个数经过一些运算能是否你循环下去的问题
        """
        if head is None or head.next is None:
            return None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if slow != fast:
            return None

        # Phase 2
        while head != slow:
            head = head.next
            slow = slow.next
        return head

    # 判断两个链表是否交汇与一点，找到这个分叉点
    @staticmethod
    def find_intersection(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        if head_a is None or head_b is None:
            return None
        tail_a = head_a
        while tail_a.next:
            tail_a = tail_a.next
        # 先把其中一条链的头尾相连，将这题转为寻找另一条链表的环的入口问题
        tail_a.next = head_a
        res = Solution.find_cycle_intersect(head_b)
        # 由于leetcode要求不能修改输入的链表，所以最后要剪掉tail_a和head_a之间的连接
        tail_a.next = None
        return res

    @staticmethod
    def find_intersection_o1_solution_2(head_a: ListNode, head_b: ListNode) -> ListNode:
        """
        假设head_a到交点的长度是a, head_b到终点的长度是b, 交点到终点的长度是y
        利用 A+B=B+A 的规律: a走到头后从起点b开始走，b走到头后从起点a开始走，大家交错的走走两趟之后一定相遇在交点
        因为 A走的路径是: a+y+b, B走的路径是: b+y+a
        FIXME 当两个链表长度相差为1且不相交时复杂度直接变为O(n^2);因为两个链表不相交，长度相差为1，大概要循环n轮链表的长度，两个才能都是尾指针NULL，才能结束循环
        """
        a, b = head_a, head_b
        while a != b:
            a = a.next if a else head_b
            b = b.next if b else head_a
        return a
