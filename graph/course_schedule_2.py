import unittest
import collections
from typing import List


def course_order(courses_count: int, prerequisites: List[List[int]]) -> List[int]:
    """
    prerequisites可以理解成一种简单的有向图邻接表(adjacency list)
    Input: 4, [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,1,2,3] or [0,2,1,3]
    """
    # index: course_id, value: indegree's courses id
    courses_indegree = []
    # index: course_id, value: next_course require current course_id
    next_courses: List[List[int]] = []
    for _ in range(courses_count):
        courses_indegree.append(0)
        next_courses.append([])

    for course_id, pre_course_id in prerequisites:
        courses_indegree[course_id] += 1
        next_courses[pre_course_id].append(course_id)
    zero_indegree_queue = collections.deque()
    for course_id in range(courses_count):
        if courses_indegree[course_id] == 0:
            zero_indegree_queue.append(course_id)
    learn_order = []
    learn_order_len = 0
    while zero_indegree_queue:
        course_id = zero_indegree_queue.popleft()
        learn_order.append(course_id)
        learn_order_len += 1
        for next_course_id in next_courses[course_id]:
            courses_indegree[next_course_id] -= 1
            if courses_indegree[next_course_id] == 0:
                zero_indegree_queue.append(next_course_id)
    # 图中有死循环，不能完整地学完课程
    if learn_order_len != courses_count:
        return []
    return learn_order


class Testing(unittest.TestCase):
    TEST_CASES = [
        (2, [[1, 0]], [0, 1]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3])
    ]

    def test_course_order(self):
        for courses_count, prerequisites, learn_order in self.TEST_CASES:
            self.assertEqual(learn_order, course_order(courses_count, prerequisites))
