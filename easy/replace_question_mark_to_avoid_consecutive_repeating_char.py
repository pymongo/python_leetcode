import unittest


class Solution(unittest.TestCase):
    def test(self):
        test_cases = [
            ("?zs", "azs"),
            ("ubv?w", "ubvaw"),
            ("j?qg??b", "jaqgacb"),
            ("??yw?ipkj?", "abywaipkja"),
        ]
        for s, expected in test_cases:
            self.assertEqual(expected, self.f(s))

    @staticmethod
    def f(s: str) -> str:
        res = []
        n = len(s)
        for i in range(n):
            if s[i] == '?':
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if i > 0 and res[i - 1] == c:
                        continue
                    if i < n - 1 and s[i + 1] == c:
                        continue
                    res.append(c)
                    break
            else:
                res.append(s[i])
        return ''.join(res)
