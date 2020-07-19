"""
https://leetcode.com/problems/zigzag-conversion/
"""
from typing import List, Tuple
# from mydbg import dbg
import unittest


def solution(s: str, rows: int) -> str:
    if rows == 1:
        return s
    size = len(s)
    arr = [[''] * size for _ in range(rows)]
    # N型号填值方向，is_up=true表示斜着向上
    is_up = False
    i, j = 0, 0
    for char in s:
        if is_up and i == 0:
            is_up = False
        if not is_up and i == rows - 1:
            is_up = True

        arr[i][j] = char

        if is_up:
            i -= 1
            j += 1
        else:
            i += 1

    result = ""
    for row in arr:
        # print(row)
        result += "".join(row)
    return result


# Runtime: 44 ms, faster than 99.27%
def best_solution(s: str, rows: int) -> str:
    if rows <= 1:
        return s
    last_row = rows - 1
    # 实际上也是用二维数组的思路，不过字符串可以拼接
    arr = ["" for _ in range(rows)]
    i, flag = 0, -1
    for char in s:
        arr[i] += char
        if i == 0 or i == last_row:
            flag = -flag
        i += flag
    return "".join(arr)


class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[str, int, str]] = [
        ("LEETCODEISHIRING", 3, "LCIRETOESIIGEDHN")
    ]

    def test(self):
        for s, rows, expected in self.TEST_CASES[:]:
            self.assertEqual(expected, solution(s, rows))
