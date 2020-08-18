class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for _ in range(n):
            res ^= start
            start += 2
        return res