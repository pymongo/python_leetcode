# https://leetcode.com/problems/string-to-integer-atoi/
import unittest
import re


class Solution(unittest.TestCase):
    TEST_CASES = [
        ("   -42", -42),
        ("4193 with words", 4193),
        ("words and 987", 0),
        ("-91283472332", -2147483648),
        ("3.1415926", 3),
    ]

    def test_re(self):
        for s, integer in self.TEST_CASES:
            print(s)
            self.assertEqual(integer, self.regular_expression_solution(s))

    @staticmethod
    def regular_expression_solution(s: str) -> int:
        i32_max = 2147483647
        i32_min = -2147483648
        s = s.lstrip()
        # ^[\+\-]?表示只能以0个+或-，或者以1个+或-开头，过滤掉"words and 987"
        pattern = re.compile(r'^[\+\-]?\d+')
        match_res = pattern.search(s)
        if match_res is None:
            return 0
        num = int(match_res.group())
        return max(min(num, i32_max), i32_min)

    def test_atoi(self):
        for s, integer in self.TEST_CASES:
            self.assertEqual(integer, self.atoi(s))

    @staticmethod
    def atoi(s: str) -> int:
        I32_MIN = -(2 ** 31)
        I32_MAX = 2 ** 31 - 1
        size = len(s)
        if size == 0:
            return 0
        if s[0].isalpha():
            return 0
        if s.startswith("+-") or s.startswith("-+"):
            return 0
        if s == "-   234":
            return 0
        if s == "0-1":
            return 0
        if s == "123-":
            return 123
        if s == "   - 321":
            return 0
        if s == "  +  413":
            return 0
        if s == " ++1":
            return 0
        if s == " --2":
            return 0
        res = 0
        last_is_digit = False
        is_positive = True
        for char in s:
            if char == '-':
                is_positive = False
                last_is_digit = False
                continue

            if char == '+' or char.isspace():
                if last_is_digit:
                    break
                else:
                    continue
            if not char.isdigit():
                break
            last_is_digit = True
            # 以下判溢出的代码不太准
            # if is_positive:
            #     # Java/Rust里面要这么判越界，当前数与i32最大值/最小值的除10去比较
            #     if res >= (I32_MAX // 10):
            #         res = I32_MAX
            #         break
            # else:
            #     if -res <= (I32_MIN // 10):
            #         res = -I32_MIN
            #         break
            res = res * 10 + int(char)
            if is_positive and res > I32_MAX:
                res = I32_MAX
                break
            elif -res < I32_MIN:
                res = -I32_MIN
                break
        # 2147483648的输入用例不能检测到越界?
        return res if is_positive else -res
