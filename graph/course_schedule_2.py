import unittest
import collections
from typing import List


class Course:
    def __init__(self):
        # self.id = course_id
        self.pre_courses = []
        self.next_courses = []
        self.indegree = 0


def course_order(courses_count: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Input: 4, [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,1,2,3] or [0,2,1,3]
    """
    # size = len(prerequisites)
    # index: course_id, value: indegree's courses id
    courses: List[Course] = [Course() for _ in range(courses_count)]
    for course_id, pre_course_id in prerequisites:
        courses[pre_course_id].next_courses.append(course_id)
        courses[course_id].pre_courses.append(pre_course_id)
        courses[course_id].indegree += 1
    queue = collections.deque()
    for course_id in range(courses_count):
        if courses[course_id].indegree == 0:
            queue.append(course_id)
    learn_order = []
    learn_order_len = 0
    while queue:
        course_id = queue.popleft()
        learn_order.append(course_id)
        learn_order_len += 1
        for next_course_id in courses[course_id].next_courses:
            courses[next_course_id].indegree -= 1
            if courses[next_course_id].indegree == 0:
                queue.append(next_course_id)
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
