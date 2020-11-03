import unittest


class Solution(unittest.TestCase):
    TESTCASES = [
        # 3! + 2!
        ("00010011", 9),
        ("010010", 5),
    ]

    def test_two_pointers(self):
        for s, count in self.TESTCASES:
            self.assertEqual(count, self.batch_count(s))

    def test_batch_count(self):
        for s, count in self.TESTCASES:
            self.assertEqual(count, self.batch_count(s))

    @staticmethod
    def two_pointers(s: str) -> int:
        size = len(s)
        if size == 0:
            return 0

        count = 0
        j = 1
        for i in range(size):
            if s[i] != '0':
                continue
            j = max(j, i + 1)
            while j < size and s[j] == '0':
                j += 1
            count += j - i

        return count

    # 批量数比双指针快得多，如果找不到批量数的公式(例如我之前错误理解成阶乘，用双指针也是可以的)
    @staticmethod
    def batch_count(s: str) -> int:
        size = len(s)
        if size == 0:
            return 0

        count = 0
        L, R = 0, 0
        while R < size:
            if s[R] == '1':
                # 注意这是等差数列，长度为3的子串有3+2+1=3*4//2种
                temp_len = R - L
                count += temp_len * (temp_len + 1) // 2
                L = R + 1
            R += 1
        if L < size and s[R-1] == '0':
            temp_len = R - L
            count += temp_len * (temp_len + 1) // 2
        return count
