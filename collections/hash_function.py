import unittest


# HASH_SIZE = 1000

# 这个计算的思路和rolling hash基本一样
def hash_function(key: str, HASH_SIZE: int) -> int:
    result = 0
    for letter in key:
        # 取模过程要使用同余定理避免溢出: (a b ) % MOD = ((a % MOD) (b % MOD)) % MOD
        result = (result * 33 + ord(letter)) % HASH_SIZE
    return result


class Testing(unittest.TestCase):
    TESTCASES = [
        ("abcd", 1000, 978),
        ("abcd", 100, 78),
    ]

    def test(self):
        for key, hash_size, index in self.TESTCASES:
            self.assertEqual(index, hash_function(key, hash_size))
