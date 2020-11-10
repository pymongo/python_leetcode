import unittest


class Solution(unittest.TestCase):
    TEST_CASES = [
        # 其实就数0和1分界处，左右两侧0和1个数的最小值
        ("100111", 3),
        # ("00110011", 6),
    ]

    @staticmethod
    def count_zero_one_equal_substr(s: str) -> int:
        """
        L: last_count
        C: current count

        1. last=0, curr=1, ans+=0
        | |1|00|111|
             ^
         L|C|

        2. [End of loop]last=1, cur=2, ans+=1
        | |1|00|111|
                ^
           L| C|

        3. out of loop
        | |1|00|111|
                    ^
              L|  C|
        """
        ans = 0
        last_count = 0
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                print(last_count, count)
                ans += min(last_count, count)
                last_count = count
                count = 1
        ans += min(last_count, count)
        return ans

    def test(self):
        for s, substr_count in self.TEST_CASES:
            self.assertEqual(substr_count, self.count_zero_one_equal_substr(s))
