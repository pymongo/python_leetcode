# 这种题无非就ASCII做数组或哈希表
class Solution:
    @staticmethod
    def numJewelsInStones(J: str, S: str) -> int:
        jewels = set(J)
        count = 0
        for stone in S:
            if stone in jewels:
                count += 1
        return count
        # 以下是网友分享的一行解法
        # return sum(S.count(i) for i in J)
